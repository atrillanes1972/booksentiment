import re

with open ("miracle_in_the_andes.txt", "r", encoding='utf-8') as file:
    book = file.read()

#print(book, end='')
# without RE expressions
#print(book.count("Chapter"))

# with RE
pattern = re.compile("Chapter [0-9]+")
findings = re.findall(pattern,book)
print(len(findings))

# Sentences where the word:'love' was used
pattern = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
findings = re.findall(pattern,book)
#for finds in findings:
#    print(finds)
print(len(findings))

# What are the most used words?
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern,book.lower())
print(len(findings))

d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1
#print(d)
d_list = [(value, key) for key, value in d.items()]
sorted = sorted(d_list, reverse=True)
print(sorted)

# Paragraphs with word love in it.
pattern = re.compile("[^\n]+love[^\n]+")
findings = re.findall(pattern,book)
print(findings)

# Extracting titles
pattern = re.compile("[a-zA-Z ,]+\n\n")
findings = re.findall(pattern,book)
findings = [item.strip("\n\n") for item in findings]
print(findings)

# Extracting titles w/o using strip against breaklines
pattern = re.compile("([a-zA-Z ,]+)\n\n")
findings = re.findall(pattern,book)
print(findings)

# Function to grep for a word and its number of occurance.
def find_word(w):
    pattern = re.compile("[a-zA-Z]+")
    findings = re.findall(pattern, book.lower())
    #print(len(findings))

    d = {}
    for word in findings:
        if word in d.keys():
            d[word] = d[word] + 1
        else:
            d[word] = 1
    try:
        return d[w]
    except:
        return f'The book does not contain the word "{w}"'

print(find_word("love"))
