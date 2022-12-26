text = 'Hello hello African people who are amazing'

tArray = text.split()

tDict = {}

for word in text:
    if word not in tDict:
        tDict[word] = 1
    else:
        tDict[word] = tDict[word] + 1


print(list(tDict))
print(tDict.items())
print(tDict.values())
print(tDict.keys())