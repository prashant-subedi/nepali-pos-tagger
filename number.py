corpus =[]
from nltk import word_tokenize
from nltk.corpus import  indian
import re
from  nltk.corpus import brown

with open("corpus/00ne_pos.txt") as corpus0:
    k = 0
    for i in corpus0:

        i=i[:-1]
        words = re.split(r"<.{2,4}>", i)
        tags = re.findall(r"<.{2,4}>",i)
        remove_space=[]
        for i in words:
            k+=1
            remove_space.append(i.strip())

        corpus.append([(i,j[1:-1]) for i,j in zip(remove_space,tags)])
print("Number of words in 00ne_pos = ",k)

k = 0
with open("corpus/01ne_pos.txt") as corpus1:
    for i in corpus1:

        i=i[:-1]
        i = i.replace(" ","")
        words = re.split(r"<.{2,4}>", i)
        tags = re.findall(r"<.{2,4}>",i)
        for i in words:
            k += 1
            remove_space.append(i.strip())

        corpus.append([(i,j[1:-1]) for i,j in zip(remove_space,tags)])
print("Number of words in 01ne_pos = ",k)

k = 0
with open("corpus/02ne_pos.txt") as corpus2:
    for i in corpus2:

        i=i[:-1]
        i = i.replace(" ","")
        words = re.split(r"<.{2,4}>", i)
        tags = re.findall(r"<.{2,4}>",i)
        for i in words:
            k += 1
            remove_space.append(i.strip())
        corpus.append([(i, j[1:-1]) for i, j in zip(remove_space, tags)])
print(len(corpus))
print("Number of words in 02ne_pos = ",k)
b=set()
#To find the number of classes in the dataset
for i in corpus:
    for j in i:
        b.add(j[1])
print(b)
print(len(b))