import spacy
import sys
import json

nlp = spacy.load("de_core_news_sm")
nlp.max_length = 2000000

fn = sys.argv[1]

sentences = [sentence.text for sentence in nlp(open(fn).read()).sents if not sentence.text.isspace()]

f = open(fn[:-3] + "json", "w")

json.dump(sentences, f)