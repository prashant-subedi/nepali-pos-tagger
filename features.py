
from  sklearn.preprocessing import  LabelEncoder,OneHotEncoder
import numpy as np


####We are going to use the following feature
# 1. Tag of Word t-2
# 2. Tag of Word t-1
# 3. Tag of Word t+1
# 4. Tag of Word t+2

def data_or_empty(l,i):
    try:
        return l[i][1]
    except IndexError:
        return "EMT"

def extract_feature(data):

    X = []
    Y = []
    for i in data:
        for x,y in enumerate(i):
            X.append(
                [

                data_or_empty(i,x - 4),
                 data_or_empty(i, x - 3),
                 data_or_empty(i,x - 2),
                 data_or_empty(i, x - 1),
                 data_or_empty(i, x + 1),
                 data_or_empty(i, x + 2),
                 data_or_empty(i, x + 3),
                 data_or_empty(i, x + 4),


                 ]
            )
            Y.append(y[1])

    for i in zip(X,Y):
        # print(i)
        pass
    return  X,Y

def set_encoder(Y):
    label_encoder = LabelEncoder()
    Y = label_encoder.fit_transform(Y + ["EMT"])
    Y = Y[:-1]
    hot_encoder = OneHotEncoder(sparse=False)
    Y = hot_encoder.fit(Y.reshape(-1, 1))
    return label_encoder,hot_encoder

def encode_features(X,Y,label_encoder,hot_encoder):
    # Below is a Hack to include EMT in the encoding

    Y = label_encoder.transform(Y )
    # This is computationally expensive task
    X = np.array([label_encoder.transform(i) for i in X])
    Y = hot_encoder.transform(Y.reshape(-1, 1))

    Z = np.array(hot_encoder.transform(X[:, 0].reshape(-1, 1)))
    for i in range(1, len(X.T)):
        Z = np.append(Z, np.array(hot_encoder.transform(X[:, i].reshape(-1, 1))), axis=1)

    return Z,Y
