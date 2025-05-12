import urllib.request
import os
import re
import argparse

class Simple_Tokenizer:
   def __init__(self, vocab):
      self.int_to_str = {i:value for i, value in enumerate(vocab)}
      self.str_to_int = {value:i for i, value in enumerate(vocab)}
    
   def encode(self, tokens):
    self.token_ids = [self.str_to_int.get(item) if self.str_to_int.get(item) is not None else self.str_to_int.get('<unk_token>') for item in tokens ]
   def decode(self):
    decoded_list=[self.int_to_str.get(item) for item in self.token_ids]
    print(decoded_list[:20])


def preprocess(file_name , is_vocab):
   with open(file_name, "r" )as file_object:
    raw_text = file_object.read()
    print(len(raw_text))
    pre_processed = re.split(r'([.,:;?()"_!\']|--|\s)', raw_text)
    pre_processed = [item.strip() for item in pre_processed if item.strip() ]
    if is_vocab:
        all_words = sorted(set(pre_processed))
        return all_words
    else:
       return pre_processed
        
if __name__== "__main__":

    ## make a parser
    ## should take a file for building vocabulary
    ## should a take as input
    parser=argparse.ArgumentParser(description='taking vocan and input files for embeddings')
    parser.add_argument('-v', '--vocab', required =False, default= 'vocab.txt', type=str, help='vocab file')
    parser.add_argument('-i', '--input', required =False, type=str,default= 'sample_input.txt', help='input file')
    args = parser.parse_args()

    vocab=preprocess(args.vocab , True)
    vocab.append('<unk_token>')
    tokens=preprocess(args.input, False)

    Tokenizer_object = Simple_Tokenizer(vocab)
    Tokenizer_object.encode(tokens)
    Tokenizer_object.decode()





   
