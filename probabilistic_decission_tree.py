# Train a statistical tagger.
# Mark Amiguous data
# Make a decision tree of each amabigious class
from features import data_or_empty, set_encoder, encode_features,extract_feature
import  analytics,corpus
from  corpus import load_corpus
import  numpy as np

class AmbigiousClass:
    def __init__(self,name):
        self.name = name
        self.X = []
        self.Y = []
        self.word_list =  set()

    def set_encoders(self,le,oh):
        self.label_encoder = le
        self.onehot_encoder = oh

    def get_encoder(self):
        #This encoder is only for Y values, encode X using a global encoder
        return self.label_encoder, self.onehot_encoder

    def add_XY(self,X,Y):
        self.X.append(X)
        self.Y.append(Y)

    def get_XY(self):
        return self.X,self.Y

    def add_word(self,word):
        self.word_list.add(word)

    def get_word(self):
        return self.word_list

    def set_clf(self,clf):
        self.clf = clf

    def get_clf(self):
        return self.clf

from sklearn.tree import DecisionTreeClassifier
statistic = analytics.load_analytics()
heighest_probabilty = {}

for i in statistic:
    heighest_probabilty[i] = max(statistic[i].items(),key=lambda x:x[1])[0]

train = corpus.load_corpus()
X_train_raw, Y_train_raw = extract_feature(data=train)

#Global label_encoder to encode X values
global_label_encoder,global_hot_encoder = set_encoder(Y_train_raw)

# print(train)
# Identify the ambiguity classes
amb_class = {}
for i in train:
    for x,y in enumerate(i):
        #If the word only has one tagging, we don't need a classifier
        if len(statistic[y[0]]) == 1:
            pass
        #If there is an ambiguity, we need a decission tree classifier

        else:
            cls = sorted(statistic[y[0]])
            cls_string = "-".join(cls)
            if cls_string not in amb_class:
                amb_class[cls_string] = AmbigiousClass(cls_string)
            amb_class[cls_string].add_XY(
                (data_or_empty(i,x - 3),
                data_or_empty(i,x - 2),
                data_or_empty(i, x - 1),
                data_or_empty(i, x + 1),
                data_or_empty(i, x + 2),
                data_or_empty(i, x  + 3)),
                y[1]
                )
            amb_class[cls_string].add_word(y[0])


amb_classifier = {}


for i,j in amb_class.items():
    X_raw ,Y_raw = j.get_XY()

    print(i,len(X_raw),len(Y_raw), j.get_word())

    print("*************************************")
    Z = []
    label_encoder,hot_encoder = set_encoder(Y_raw)
    j.set_encoders(label_encoder,hot_encoder)

    #Encoding X and Y using different encodings
    Y = label_encoder.transform(Y_raw)
    Y = hot_encoder.transform(Y.reshape(-1, 1))

    # This is computationally expensive task
    X = np.array([global_label_encoder.transform(i) for i in X_raw])
    Z = np.array(global_hot_encoder.transform(X[:, 0].reshape(-1, 1)))

    for i in range(1, len(X.T)):
        Z = np.append(Z, np.array(global_hot_encoder.transform(X[:, i].reshape(-1, 1))), axis=1)

    clf = DecisionTreeClassifier()
    clf.fit(X,Z)
    j.set_clf(clf)


#Now We Will Do The Testing

test = corpus.load_corpus(last=True)
test_dict = []
for i in test:
    for j in i:
        test_dict.append(j)

hit = 0
miss = 0
unknwon = 0
ambiguity_miss = 0
unknwon_ambiguity = 0
a = 1

for i in test_dict:
    try:
        if len(statistic[i[0]]) == 1:
            if heighest_probabilty[i[0]] == i[1]:
                hit+=1
            else:
                miss+=1
        else:
            if i[1] in statistic[i[0]]:
                clf = amb_class["-".join(sorted(statistic[i[0]]))].get_clf()
                print("")
            else:
                #No use of classifiying since the program not be able to classify
                miss+=1
    except KeyError:
        miss+=1
        unknwon+=1

