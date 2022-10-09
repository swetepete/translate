import spacy
import sys
import json

nlp = spacy.load("de_core_news_sm")
nlp.max_length = 2000000

fn = sys.argv[1]

f = open(fn)

sentences = [sentence.text for sentence in nlp(f.read()).sents if not sentence.text.isspace()]

data = {"current_loc": 0, "sentences": sentences}

f = open(fn[:-3] + "json", "w")

json.dump(data, f)
