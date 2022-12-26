word = 'Coming to a realization of the most important things in life helps put everything into perspective.'

wordArray = word.split()

print(wordArray)

wordDict = dict()

for word in wordArray:
    if word not in wordDict:
        wordDict[word] = 1
    else:
        wordDict[word] = wordDict[word] + 1

print(wordDict)

for number, key in wordDict.items():
    print(number, key)
