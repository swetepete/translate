import json
from glob import glob
import deepl

# what probably makes the most sense is keeping your deepl api key as a repo secret so when you clone this it gets inserted here 

segments = glob("*.json")

f = open(segments, "rw")

lines = json.load(f)

# I would love to write this in a new way

# even further, this should be a special iteration function which iterates selectively - it always jumps to the next blank segment 
iterate(lines, l, body(l))

def body(l):

  print(l["de"])

  input_switch_loop:

    ".": 
      print(deepl(l["de"]))

    else:
      # current dict value gets written
      # like "for key, value in dict"
      # json.dump(lines, f)






