import sys
import os
import json
import deepl
import textwrap

fn = sys.argv[1]

f = open(fn, "r+")

data = json.load(f)

current_loc = data["current_loc"]

sentences = data["sentences"]

translator = deepl.Translator(os.environ["DEEPL_API"])

for sentence in sentences[current_loc:]:
  
  term_width = os.get_terminal_size().columns
  
  print("\n" + textwrap.fill(sentence, term_width) + "\n\n" + ("-" * term_width) + "\n")
  
  if input() == "exit":
    exit()
  else:
    print("\n" + textwrap.fill(translator.translate_text(sentence, target_lang="EN-US").text, term_width) + "\n\n" + ("-" * term_width) + "\n")
    
  if input() == "exit":
    exit()
  else:
    current_loc += 1
    data["current_loc"] = current_loc
    f.seek(0)
    json.dump(data, f)
    f.truncate()
  
  
  
  
  
  
  
  
  
  
