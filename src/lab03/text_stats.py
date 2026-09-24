import sys 
from src.lib.text import normalize, tokenize, count_freq, top_n

text = open(0, encoding='utf-8').read()
# text = sys.stdin.read()
normal_text = normalize(text)
tokens = tokenize(normal_text)
words_cnt = count_freq(tokens)
print(f'''
Всего слов: {len(tokens)}
Уникальных слов: {len(words_cnt)}
Топ-5:''')
# обычный вывод
# for tops in top_n(words_cnt):
#     print(f'{tops[0]}:{tops[1]}')
top_words = top_n(words_cnt)

max_len = max(max([len(word) for word in top_words]), len('слово'))
print(max_len)
print(f'{'слово':<{max_len}} | частота')

