import json
import spacy
import sys
import re

# run this script by passing the ebook title
book_title = sys.argv[1]

text = open(book_title)

# this names the segments file after the ebook title with the correct suffix
if book_title[-4:] == ".txt":
  filename = book_title[:-4] + ".json"
else:
  filename = book_title + ".json"

f = open(filename, "w")



nlp = spacy.load("de_core_news_sm")

doc = nlp(text)

# Spacy segmentation leaves NSU's (non-sentential units) next to each other as a single segment. We want to split them up.

elements = [element for sentence in doc.sents for element in re.compile("").split(sentence.text)]

# pair each sentence with a slot for its translation

segments = [{"de": sentence, "en": ""} for sentence in elements]

json.dump(segments, f)

f.close()
