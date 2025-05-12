import urllib.request
import os
import re

class Simple_Tokenizer:
   def __init__(self, vocab):
      self.int_to_str = [{i:value} for i, value in enumerate(vocab)]
      self.str_to_int = vocab
    
   def encode(self, file_name):
      with open(file_name , "r") as if_file:
         raw_text = if_file.read()
      print(len(raw_text))



if __name__== "__main__":
    ## make a parser
    ## should take a file for building vocabulary
    ## should a take as input
    with open("vocab.txt", "r" )as file_object:
        raw_text = file_object.read()
        print(len(raw_text))

    pre_processed = re.split(r'([.,:;?()"_!\']|--|\s)', raw_text)
    pre_processed = [item.strip() for item in pre_processed if item.strip() ]
    all_words = sorted(set(pre_processed))
    Tokenizer_object = Simple_Tokenizer(all_words)
    Tokenizer_object.encode("sample_input.txt")





   
