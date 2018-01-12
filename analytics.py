import corpus
s = 0
data = corpus.load_corpus()
print(len(data))
stat = {}
s= 0
for i in data:
    for j in i:
        if j == ('को', 'JJ'):
            s+=1
print(s)
for i in data:
    for j in i:
        if j[0] not in stat:
            stat[j[0]] = {j[1]:1}
        elif j[1] not in stat[j[0]]:
            stat[j[0]][j[1]]=1
        else:
            stat[j[0]][j[1]] +=1
s = 0
for key, value in sorted(stat['को'].items(), key=lambda k:k[1], reverse= True ):
    print ("%s: %s" % (key, value))
    s+=value
print(s)