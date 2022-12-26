summary = 'the book consists of various forms of art that the Piraha people used in the past'

sDict ={}
sList = summary.split()

for word in sList:
    sDict[word] = sDict.get(word, 0) + 1

print(sDict)

for key, number in sDict.items(): 
    print(key, number)