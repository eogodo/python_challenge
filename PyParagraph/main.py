import os
import re

total_words = 0
total_letters = 0 
total_sentences = 0
characters = 0

import_path = os.path.join("raw_data", "paragraph_2.txt")

with open(import_path,'r') as text:
    
    for lines in text:
        words=len(lines.split())
        total_words += words 
        sentences = len(re.split("(?<=[.!?]) +", lines))
        total_sentences += sentences
        characters+=len(lines)-(words-1)
        
    avg_letters = characters/total_words
    avg_sen_len = total_words/total_sentences

    print(f'Approximate Word Count: {total_words}')
    print(f'Approximate Sentence Count: {total_sentences}')
    print(f'Average Letter Count: {avg_letters}')
    print(f'Average Sentence Length: {avg_sen_len}')