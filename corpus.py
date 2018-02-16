import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


def load_corpus(last = False, test = 2, all = False):
    corpus = []
    remove_space = []
    if (last == True and test == 0) or (last == False and test != 0) or (all == True):
        with open("corpus/00ne_pos.txt") as corpus0:
            for i in corpus0:
                remove_space = []
                words = re.split(r"<.{2,4}>", i)
                tags = re.findall(r"<.{2,4}>", i)
                for i in words:
                    remove_space.append(i.strip())
                corpus.append([(i, j[1:-1]) for i, j in zip(remove_space, tags)])
                #print([(i, j[1:-1]) for i, j in zip(remove_space, tags)])
    if (last == True and test == 1) or (last == False and test != 1) or (all == True) :
        with open("corpus/02ne_pos.txt") as corpus1:
            for i in corpus1:
                remove_space = []
                i = i[:-1]
                i = i.replace(" ", "")
                words = re.split(r"<.{2,4}>", i)
                tags = re.findall(r"<.{2,4}>", i)
                for i in words:
                    remove_space.append(i.strip())
                corpus.append([(i, j[1:-1]) for i, j in zip(remove_space, tags)])
    if (last == True and test == 2) or (last == False and test != 2)or (all == True):
        with open("corpus/01ne_pos.txt") as corpus2:
            for i in corpus2:
                remove_space = []
                i = i[:-1]
                i = i.replace(" ", "")
                words = re.split(r"<.{2,4}>", i)
                tags = re.findall(r"<.{2,4}>", i)
                for i in words:
                    remove_space.append(i.strip())
                corpus.append([(i, j[1:-1]) for i, j in zip(remove_space, tags)])
    return corpus