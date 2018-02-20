# Train a statistical tagger.
# Mark Amiguous data
# Make a decision tree of each amabigious class
from features import data_or_empty, set_encoder, encode_features,extract_feature
import  analytics,corpus
from  corpus import load_corpus
import  numpy as np
import sys
from dictionary import  conversion
from AmbigiousClass import AmbigiousClass

try:
    TEST = int(sys.argv[1])
except ValueError:
    print("Enter 0,1,2 to specify testing document")
    exit()
except IndexError:
    TEST = 2

    #def get_
from sklearn.tree import DecisionTreeClassifier
train = corpus.load_corpus(all=True)
statistic = analytics.load_analytics(train)
heighest_probabilty = {}

for i in statistic:
    heighest_probabilty[i] = max(statistic[i].items(),key=lambda x:x[1])[0]

X_train_raw, Y_train_raw = extract_feature(data=train)

#Global label_encoder to encode X values
global_label_encoder,global_hot_encoder = set_encoder(Y_train_raw)
print("Training Global Classifer ....")
X_train,Y_train = encode_features(X_train_raw,Y_train_raw,global_label_encoder,global_hot_encoder)
global_clf = DecisionTreeClassifier()
global_clf.fit(X_train,Y_train)
print("Completed")

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
                (data_or_empty(i, x - 4),
                data_or_empty(i,x - 3),
                data_or_empty(i,x - 2),
                data_or_empty(i, x - 1),
                data_or_empty(i, x + 1),
                data_or_empty(i, x + 2),
                data_or_empty(i, x  + 3),
                data_or_empty(i, x + 4)),
            y[1]
                )
            amb_class[cls_string].add_word(y[0])


amb_classifier = {}

print("Trainning Ambigious Class Classifiers")
for i,j in amb_class.items():
    X_raw ,Y_raw = j.get_XY()

#    print(i,len(X_raw),len(Y_raw), j.get_word())
#
#    print("*************************************")
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
    clf.fit(Z,Y)
    j.set_clf(clf)

#print(Z.shape)
print("Completed")
def get_labels(l,i):
    try:
        return  l[i]
    except IndexError:
        return "EMT"


import pickle
amb_class_pkl = open("data/amb_cls.pkl","wb")
pickle.dump(amb_class,amb_class_pkl)
amb_class_pkl.close()

global_label_encoder_pkl = open("data/global_label_encoder.pkl","wb")
pickle.dump(global_label_encoder,global_label_encoder_pkl)
global_label_encoder_pkl.close()

global_hot_encoder_pkl = open("data/global_hot_encoder.pkl","wb")
pickle.dump(global_hot_encoder,global_hot_encoder_pkl)
global_hot_encoder_pkl.close()

statistic_pkl = open("data/statistic.pkl","wb")
pickle.dump(statistic,statistic_pkl)
statistic_pkl.close()

heighest_probabilty_pkl = open("data/heighest_probabilty.pkl","wb")
pickle.dump(heighest_probabilty,heighest_probabilty_pkl)
heighest_probabilty_pkl.close()

global_clf_pkl = open("data/global_clf.pkl","wb")
pickle.dump(global_clf,global_clf_pkl)
global_clf_pkl.close()

