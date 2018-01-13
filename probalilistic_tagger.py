# A simple probablistic tagger
# The goal is to beat this accuracy using ML
import  analytics,corpus
statistic = analytics.load_analytics()
heighest_probabilty = {}
for i in statistic:
    heighest_probabilty[i] = max(statistic[i].items(),key=lambda x:x[1])[0]
test = corpus.load_corpus(last=True)
test_dict = []
for i in test:
    for j in i:
        test_dict.append(j)

hit = 0
miss = 0
unknwon = 0
ambiguity_miss = 0
for i in test_dict:
    try:
        if heighest_probabilty[i[0]] == i[1]:
            hit+=1
        else:
            if i[0] in heighest_probabilty[i[0]]:
                ambiguity_miss+=1
            miss+=1
    except KeyError:
        miss+=1
        unknwon+=1


print("accuracy:", hit/(hit+miss))
print("total:",(hit+miss))
print("ambiguity_miss",ambiguity_miss)
print("unknown:", unknwon)
print("total hit,total miss(including unkown and ambiguity):", hit,miss)

#print(heighest_probabilty["मेरो"])
#print(test_dict)