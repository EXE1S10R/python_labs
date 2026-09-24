import sys 
from src.lib.text import normalize, tokenize, count_freq, top_n


text = sys.stdin.read()
normal_text = normalize(text)
tokens = tokenize(normal_text)
words_cnt = count_freq(tokens)