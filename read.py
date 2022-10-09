import deepl
import spacy
import os
import sys

nlp = spacy.load("de_core_news_sm")
nlp.max_length = 2000000
sentences = [sentence.text for sentence in nlp(open(sys.argv[1]).read()).sents if sentence.text.isspace()]


translator = deepl.Translator(os.environ["DEEPL_API"])


for sentence in sentences:
  input(sentence + "\n" + ("-" * os.get_terminal_size().columns))
  input(translator.translate_text(sentence, target_lang="EN-US").text + "\n" + ("-" * os.get_terminal_size().columns))
