
import spacy
import sys
import json

def flag_terminals(ls, depth):

  output = []

  for element in ls:


    if not isinstance(element, list) and len(list(element.children)) == depth:

      output.append([element])

    else:
      
      output.append(element)

  return output

def words_are_siblings(word1, word2):

  return word1 == word2.head or word2 == word1.head

def lists_are_siblings(ls1, ls2):

  for e1 in ls1:

    for e2 in ls2:

      if words_are_siblings(e1, e2):

        return True

  return False

def group_by_siblings(ls, size):

  output = []

  for index, chunk in enumerate(ls):

    if isinstance(chunk, list):

      new_sublist = chunk

      while index + 1 < len(ls) and isinstance(ls[index + 1], list) and lists_are_siblings(chunk, ls[index + 1]) and len(chunk) + len(ls[index + 1]) <= size:

        new_sublist += ls[index + 1]
                    
        del ls[index + 1]

      

      output.append(new_sublist)

    else:

      output.append(chunk)

  return output
          
def is_list_of_lists(ls):



  for element in ls:
    if not isinstance(element, list):
      return False

  return True

def pair_wise_conglomerate(chunks, size):
  output = []
  for index, chunk in enumerate(chunks):
    new_sublist = chunk
    while index + 1 < len(chunks) and len(chunk) + len(chunks[index + 1]) <= size:
      new_sublist += chunks[index + 1]
      del chunks[index + 1]
    output.append(new_sublist)

  return output  

def convert_chunks_to_segmented_strings(chunks, sentence):

  segments = []

  for chunk in chunks:
    beginning_index = chunk[0].i
    end_index = chunk[-1].i

    segment = doc[beginning_index:end_index + 1].text
    segments.append(segment)

  return segments

def return_clausal_segmentation(sentence, size):  

  chunks = [word for word in sentence]

  # before the rest happens you should accumulate on punctuation first!

  depth = 0

  while not is_list_of_lists(chunks):

    chunks = flag_terminals(chunks, depth)

    chunks = group_by_siblings(chunks, size)

    depth += 1

  chunks = pair_wise_conglomerate(chunks, size)

  segments = convert_chunks_to_segmented_strings(chunks, sentence)

  return segments



nlp = spacy.load("de_core_news_sm")
nlp.max_length = 2000000

fn = sys.argv[1]

f = open(fn)

text = f.read()

doc = nlp(text)

sentences = [sentence for sentence in doc.sents if not sentence.text.isspace()]

clauses = []

for sentence in sentences:
  new_clauses = return_clausal_segmentation(sentence, 7)
  clauses = clauses + new_clauses

data = {"current_loc": 0, "segments": clauses}

f = open(fn[:-3] + "json", "w")

json.dump(data, f)












