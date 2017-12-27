corpus =[]
from nltk import word_tokenize
from nltk.corpus import  indian
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import  train_test_split
with open("corpus/00ne_pos.txt") as corpus0:
    for i in corpus0:

        i=i[:-1]
        words = re.split(r"<.{2,4}>", i)
        tags = re.findall(r"<.{2,4}>",i)
        remove_space=[]
        for i in words:
            remove_space.append(i.strip())
        corpus.append([(i,j[1:-1]) for i,j in zip(remove_space,tags)])

with open("corpus/01ne_pos.txt") as corpus1:
    for i in corpus1:
        i=i[:-1]
        i = i.replace(" ","")
        words = re.split(r"<.{2,4}>", i)
        tags = re.findall(r"<.{2,4}>",i)
        for i in words:
            remove_space.append(i.strip())
        corpus.append([(i,j[1:-1]) for i,j in zip(remove_space,tags)])

with open("corpus/02ne_pos.txt") as corpus2:
    for i in corpus2:
        i=i[:-1]
        i = i.replace(" ","")
        words = re.split(r"<.{2,4}>", i)
        tags = re.findall(r"<.{2,4}>",i)
        for i in words:
            remove_space.append(i.strip())
        corpus.append([(i, j[1:-1]) for i, j in zip(remove_space, tags)])

Data = []
for i in corpus:
    Data.extend(i)
X = [i[0] for i in Data]
Y = [i[1] for i in Data]
#print(t)
split = len(corpus)-len(corpus)//20


tf = CountVectorizer()
t = tf.fit_transform(X).toarray()
print(t.shape)
print(len(Y))
x_train = t[:split]
x_test = t[split:]
y_train = Y[:split]
y_test =Y[split:]
from sklearn.naive_bayes import  GaussianNB
clf = GaussianNB()
clf.fit(x_train,y_train)
print("Finished Trainning")
print(clf.score(x_test,y_test))

#from nltk.tag import tnt
#tnt_pos_tagger = tnt.TnT()
#tnt_pos_tagger.train(train)

#print(word_tokenize(word_test))

#print(tnt_pos_tagger.evaluate(test))

#print(tnt_pos_tagger.tag(word_tokenize(word_test)))
