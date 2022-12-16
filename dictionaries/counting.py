counts = {}

names = ['pete', 'jan', 'pete', 'pele', 'hade', 'musa', 'pele', 'pete']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)

# simplified counting with get()
myDict = dict()

for nm in names:
    myDict[nm] = myDict.get(nm, 0) + 1
print(myDict)