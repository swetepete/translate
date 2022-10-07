import deepl
import spacy
import os
import sys

nlp = spacy.load("de_core_news_sm")
nlp.max_length = 2000000
sentences = [sentence.text for sentence in nlp(open(sys.argv[1]).read()).sents]


translator = deepl.Translator(os.environ["DEEPL_API"])


for sentence in sentences:
  input(sentence)
  input(translator.translate_text(sentence.text, target_lang="EN-US").text)
  
  
