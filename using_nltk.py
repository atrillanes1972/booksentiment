import re
import nltk
#nltk.download("stopwords")
#nltk.download("vader_lexicon")
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer


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

#print(filtered_words)

# Using nltk sentiment analyzer
analyzer = SentimentIntensityAnalyzer()
findings = analyzer.polarity_scores(book)
#print(findings)
pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)
chapters = chapters[1:]
for nr, chapter in enumerate(chapters):
    scores = analyzer.polarity_scores(chapter)
    print(nr + 1, scores)
