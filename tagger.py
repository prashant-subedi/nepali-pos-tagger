import pickle
from AmbigiousClass  import AmbigiousClass
from dictionary import conversion
import numpy as np
#Loading Classifiers
amb_class_pkl = open("data/amb_cls.pkl","rb")

amb_class = pickle.load(amb_class_pkl)

global_label_encoder_pkl = open("data/global_label_encoder.pkl","rb")
global_label_encoder = pickle.load(global_label_encoder_pkl)

global_hot_encoder_pkl = open("data/global_hot_encoder.pkl","rb")
global_hot_encoder = pickle.load(global_hot_encoder_pkl)

statistic_pkl = open("data/statistic.pkl","rb")
statistic = pickle.load(statistic_pkl)

heighest_probabilty_pkl = open("data/heighest_probabilty.pkl","rb")
heighest_probabilty = pickle.load(heighest_probabilty_pkl)


global_clf_pkl = open("data/global_clf.pkl","rb")
global_clf = pickle.load(global_clf_pkl)



def get_labels(l,i):
    try:
        return  l[i]
    except IndexError:
        return "EMT"

#Here we will classify the text:
def classify_tokenized_sentence(words,itr = 0):
    ## Initial Labeling Using Probablistic Tagger
    labeled_string = list()
    for i in words:
        try:
            labeled_string.append(heighest_probabilty[i])
        except KeyError:
			
            labeled_string.append("UNK")

    #Now Applying the Hybrid Approach
    # Now Applying the Hybrid Approach
    for i in range(itr):
        for e, i in enumerate(words):

            X_raw = ((
                get_labels(labeled_string, e - 4),
                get_labels(labeled_string, e - 3),
                get_labels(labeled_string, e - 2),
                get_labels(labeled_string, e - 1),
                get_labels(labeled_string, e + 1),
                get_labels(labeled_string, e + 2),
                get_labels(labeled_string, e + 3),
                get_labels(labeled_string, e + 4),

            ))
            X = global_label_encoder.transform(X_raw)
            X_one_hot = global_hot_encoder.transform(X.reshape(-1, 1))
            X_one_hot = X_one_hot.reshape(1, -1)

            try:
                if len(statistic[i]) == 1:
                    pass
                else:
                    amb_class_object = amb_class["-".join(sorted(statistic[i].keys()))]
                    clf = amb_class_object.get_clf()

                    # print(X_one_hot.shape)
                    pre = clf.predict(X_one_hot)
                    labeled_string[e] = amb_class_object.get_encoder()[0].inverse_transform([np.argmax(pre)])[0]
            except:
                pre = global_clf.predict(X_one_hot)
                labeled_string[e] = global_label_encoder.inverse_transform([np.argmax(pre)])[0]

    return labeled_string
    
def tokenizer(s):
    words = [x.strip() for x in s.split(" ") if x != ""]
    words_aug = []
    for i in words:

        if "हरू" in i:
            words_aug.append(i.replace("हरू",""))
            words_aug.append("हरू")
        else:
            words_aug.append(i)

    return words_aug

import sys
if len(sys.argv) <2:
	print("Enter File to Be Tagged")

try:
    with open(sys.argv[1]) as inp:
        lines = inp.read().split("।")
        lines = [i+"।" for i in lines]
        converted = ""
        for i in lines:
            words= tokenizer(i)
            op = classify_tokenized_sentence(words,3)
            converted += " ".join([i[0] +"<" + i[1]+">" for i in zip(words,op)])
except FileNotFoundError:
    print("Enter a valid file name")

with open("converted_"+sys.argv[1],"w") as op:
	op.write(converted)
