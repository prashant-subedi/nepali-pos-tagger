# Train a statistical tagger.
# Mark Amiguous data
# Make a decision tree of each amabigious class
from features import data_or_empty, set_encoder, encode_features
import  analytics,corpus
import  numpy as np
from sklearn.tree import DecisionTreeClassifier
statistic = analytics.load_analytics()
heighest_probabilty = {}
for i in statistic:
    heighest_probabilty[i] = max(statistic[i].items(),key=lambda x:x[1])[0]

train = corpus.load_corpus()

# I identify the ambiguity classes
amb_class = {}
for i in train:
    for x,y in enumerate(i):
        if len(statistic[y[0]]) == 1:
            pass
        else:
            cls = sorted(statistic[y[0]])
            cls_string = "-".join(cls)
            if cls_string in amb_class:
                amb_class[cls_string].append([
                    data_or_empty(i,x - 3),
                    data_or_empty(i,x - 2),
                    data_or_empty(i, x - 1),
                    data_or_empty(i, x + 1),
                    data_or_empty(i, x + 2),
                    data_or_empty(i, x  + 3),
                    y[1]
                ])

            else:

                amb_class[cls_string] = [[
                    data_or_empty(i, x - 3),
                    data_or_empty(i, x - 2),
                    data_or_empty(i, x - 1),
                    data_or_empty(i, x + 1),
                    data_or_empty(i, x + 2),
                    data_or_empty(i, x + 3),
                    y[1]
                    ]
                ]
X = []
amb_class_classifier = {}
for i in amb_class:
    Z = np.array(amb_class[i])
    X = Z[:,:-1]
    Y = Z[:,-1]
    label_encoder,hot_encoder = set_encoder(list(np.append(X.flatten(),Y.reshape(1,-1))))
    X_train,Y_train = encode_features(X,Y,label_encoder,hot_encoder)
    clf = DecisionTreeClassifier()
    clf.fit(X_train,Y_train)
    amb_class_classifier = clf



