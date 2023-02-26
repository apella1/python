summary = 'the book consists of various forms of art that the Piraha people used in the past'

sDict = {}
sList = summary.split()

for word in sList:
    """The functionality of the get method"""
    sDict[word] = sDict.get(word, 0) + 1

print(sDict)

for key, value in sDict.items():
    """items() returns a tuple with the key and value pairs"""
    print(key, value)
