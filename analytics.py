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

