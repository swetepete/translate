import deepl
import spacy
import sys

nlp = spacy.load("de_core_news_sm")
nlp.max_length = 2000000
sentences = nlp(open(sys.argv[1]).read()).sents


translator = deepl.Translator(sys.environ["DEEPL_API"])


for sentence in sentences:
  print(sentence)
  while x := input():
      translator.translate_text(sentence, target_lang="DE").text



