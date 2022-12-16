word = 'What a time to be alive!'
word_list = word.split()

print(word_list, len(word_list), len(word))


# passing arguments to split

poem = 'hello;new;word'
print(poem.split())

new_poem = poem.split(';')
print(new_poem)