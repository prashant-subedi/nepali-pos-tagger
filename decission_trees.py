from  features import extract_feature, set_encoder,encode_features
from  corpus import  load_corpus

from sklearn.tree import  DecisionTreeClassifier

X_train_raw, Y_train_raw = extract_feature(data=load_corpus())

label_encoder,hot_encoder = set_encoder(Y_train_raw)

X_train,Y_train = encode_features(X_train_raw,Y_train_raw,label_encoder,hot_encoder)

clf = DecisionTreeClassifier()
clf.fit(X_train,Y_train)

X_test_raw,Y_test_raw = extract_feature(load_corpus(last=True))
X_test,Y_test = encode_features(X_test_raw,Y_test_raw,label_encoder,hot_encoder)
print(clf.score(X_test,Y_test))
