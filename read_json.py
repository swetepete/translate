import sys
import os
import json
import deepl

fn = sys.argv[1]

sentences = json.load(open(fn))

translator = deepl.Translator(os.environ["DEEPL_API"])


for sentence in sentences:
  input(sentence + "\n" + ("-" * os.get_terminal_size().columns))
  input(translator.translate_text(sentence, target_lang="EN-US").text + "\n" + ("-" * os.get_terminal_size().columns))
