counts = {}

names = ['pete', 'jan', 'pete', 'pele', 'hade', 'man', 'pele', 'pete']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)

numbers = [2, 4, 5, 3, 8, 2, 0, 3, 4, 5, 1, 4, 8, 9, 2, 6, 1, 5]

numDict = {}
nDict = {}

for nm in numbers:
    numDict[nm] = nDict.get(nm, 0) + 1

print(nDict)

for number in numbers:
    if number not in numDict:
        numDict[number] = 1
    else: 
        numDict[number] = numDict[number] + 1

print(numDict)

for number, key in numDict.items():
    print(number, key)

# simplified counting with get()
myDict = dict()

for nm in names:
    myDict[nm] = myDict.get(nm, 0) + 1
print(myDict)