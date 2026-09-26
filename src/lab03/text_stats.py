from src.lib.text import normalize, tokenize, count_freq, top_n


text = open(0, encoding='utf-8').read()
if text.strip() == '':
    raise ValueError('Не был введен текст')
if_beautiful = 1    #Переменная определяющая красивый вывод


normal_text = normalize(text)
tokens = tokenize(normal_text)
words_cnt = count_freq(tokens)
top_words = top_n(words_cnt)


print(f'''
Всего слов: {len(tokens)}
Уникальных слов: {len(words_cnt)}
Топ-5:''')
if not(if_beautiful): # обычный вывод
    for tops in top_words:
        print(f'{tops[0]}:{tops[1]}')
else:   #Красивый вывод
    max_len = max(max([len(word[0]) for word in top_words]), len('слово'))
    head = f'{"слово":<{max_len}} | частота'

    print(head)
    print('-' * len(head))
    for top in top_words:
        print(f'{top[0]:<{max_len}} | {top[1]}')
    print('...')

