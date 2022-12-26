text = 'the clown ran after the car and the car ran into the tent and the tent fell onto the clown and the car'

textArray = text.split()

counts = {}

for word in textArray:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] = counts[word] + 1
        

print(counts)


# using get()
numCount = dict()

for wrd in textArray:
    numCount[wrd] = numCount.get(wrd, 0) + 1

print(numCount)

# definite loops and dictionaries
for key in numCount:
    print(key, numCount[key])


# retrieving lists of keys and values

print(list(numCount))
print(numCount.keys())
print(numCount.values())
print(numCount.items())  # returning tuples


# two iteration variables

for nm, ky in counts.items():
    print(nm, ky)