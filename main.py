from requests import get
from collections import Counter
import spacy 

nlp = spacy.load('en')

resp = get('https://cryptic-ravine-96718.herokuapp.com')
data = resp.json()
titles = [ item['title']  for item in data['news'] ]
title_string = ' '.join(titles)
doc = nlp(title_string)
words = [token.text.lower() for token in doc 
    if (not token.is_stop) and (not token.is_punct)]

freq = Counter(words)
print(freq.most_common(5))


