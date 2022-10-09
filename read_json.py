import sys
import os
import json
import deepl

fn = sys.argv[1]

f = open(fn, "r+")

data = json.load(f)

current_loc = data["current_loc"]

sentences = data["sentences"]

translator = deepl.Translator(os.environ["DEEPL_API"])

for sentence in sentences[current_loc:]:
  
  input(sentence + "\n" + ("-" * os.get_terminal_size().columns))
  input(translator.translate_text(sentence, target_lang="EN-US").text + "\n" + ("-" * os.get_terminal_size().columns))
  
  current_loc += 1
  data["current_loc"] = current_loc
  f.seek(0)
  json.dump(data, f)
  f.truncate()
  
  
