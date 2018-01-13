import corpus
def load_analytics():
    s = 0
    data = corpus.load_corpus()
    # print(len(data))
    stat = {}
    #s= 0
    # for i in data:
    #     for j in i:
    #         if j == ('को', 'JJ'):
    #             s+=1
    # print(s)

    for i in data:
        for j in i:
            if j[0] not in stat:
                stat[j[0]] = {j[1]:1}
            elif j[1] not in stat[j[0]]:
                stat[j[0]][j[1]]=1
            else:
                stat[j[0]][j[1]] +=1
    s = 0
    amb_class = {}
    amb_words = {}
    already_found = []
    for k,v in stat.items():
        if len(v) > 1:
            if set(v.keys()) in already_found:
                amb_class["-".join(sorted(v.keys()))] += sum(v.values())
                amb_words["-".join(sorted(v.keys()))].append((k,v))
            else:

                amb_words["-".join(sorted(v.keys()))] = [(k,v)]
                already_found.append(set(v.keys()))
                amb_class["-".join(sorted(v.keys()))]=sum(v.values())
                #print(k, v)
                s+=1

    for i in amb_words.items():
        # print(i)
        pass

    print("Amb Class:", s)
    print("Total Ambigious word occurences:", sum(amb_class.values()))
    print("Total:",sum([len(i) for i in data]))
    # for key, value in sorted(stat['को'].items(), key=lambda k:k[1], reverse= True ):
    #     print ("%s: %s" % (key, value))
    return stat