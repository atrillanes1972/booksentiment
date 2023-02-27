import re

with open ("miracle_in_the_andes.txt", "r", encoding='utf-8') as file:
    book = file.read()

#print(book, end='')
# without RE expressions
print(book.count("Chapter"))

# with RE
pattern = re.compile("Chapter [0-9]+")
findings = re.findall(pattern,book)
print(findings)