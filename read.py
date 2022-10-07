import deepl
import spacy
import os

nlp = spacy.load("de_core_news_sm")
nlp.max_length = 2000000
sentences = nlp(open(sys.argv[1]).read()).sents


translator = deepl.Translator(os.environ["DEEPL_API"])


for sentence in sentences:
  print(sentence)
  while x := input():
      translator.translate_text(sentence, target_lang="EN").text



