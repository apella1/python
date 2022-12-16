# find() - first occurrence

word = 'I am energized for the day'

print(word.find('ner'))

# prefixes

print(word.startswith('I'))

# upper and lower methods

print(word.upper(), word.lower())


# replace() - search and replace

happy_word = word.replace('energized', 'happy')

print(happy_word)


# stripping whitespace - lstript(), stript(), rstript(),

greeting = '  Hello Knuth  '
print(greeting)

print(greeting.lstrip())
print(greeting.strip())
print(greeting.rstrip())


# parsing and extracting

data = 'From collins.apella@students.ku.ac.ke Fri Jan 18 06:13:14 2022'

email = data.find('@')
print(email)
end = data.find(' ', email)
print(end)

host = data[email + 1: end]
print(host)

# Double splitting
info = 'From collins.apella@students.ku.ac.ke Fri Jan 18 06:13:14 2022'
pieces = info.split()
email_addr = pieces[1]
host = email_addr.split('@')
hostname = host[1]
print(hostname)