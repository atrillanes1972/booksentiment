import re
import nltk
#nltk.download("stopwords")
from nltk.corpus import stopwords


with open ("miracle_in_the_andes.txt", "r", encoding='utf-8') as file:
    book = file.read()

# What are the most used words?
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern,book.lower())
#print(len(findings))

d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1
#print(d)
d_list = [(value, key) for key, value in d.items()]
d_list = sorted(d_list, reverse=True)
#print(sorted)

english_stopwords = stopwords.words("english")
#print(english_stopwords)
filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))

print(filtered_words)