from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, top_n, count_freq
import argparse

# region Берем аргументы
parser = argparse.ArgumentParser()
parser.add_argument('--in', nargs='+', dest='input_files')
parser.add_argument('--out', nargs='+', dest='output_files')
parser.add_argument('--encoding', default='utf-8')
parser.add_argument('--per-file', default='data/lab04/report_per_file.csv')
parser.add_argument('--total', default='data/lab04/report_total.csv')
args = parser.parse_args()
'''
Пример вызова:
python -m src.lab04.text_report --in data/b.txt data/a.txt --encoding cp1251 --per-file data/report_per_file.csv --total data/report_total.csv
'''
# endregion

if args.output_files and len(args.output_files) > 1:
    raise ValueError('Сообщено слишком много файлов выхода')

if args.input_files is None:
    # region Для одного файла
    file_path = 'data/lab04/input.txt'
    text = read_text(file_path, encoding=args.encoding)
    normal_text = normalize(text)
    tokens = tokenize(normal_text)
    words_cnt = count_freq(tokens)
    top_words = top_n(words_cnt)

    if args.output_files is None:
        path = 'data/lab04/report.csv'
    else:
        path = args.output_files[0]

    all_sorted_words = top_n(words_cnt, len(words_cnt))
    write_csv(list(all_sorted_words), path, header=('word', 'count'))

    print(f'Всего слов: {len(tokens)} \n \nУникальных слов: {len(set(tokens))} \n')
    for tops in top_words:
        print(f'{tops[0]}:{tops[1]}')
    # endregion
else:
    # region Для много файлов
    per_file = [] # Здесь лежат данные в формате [file_path, word, count]
    all_cnt = {} # А тут лежит словарь где указаны частоты всех слов

    for file_path in sorted(args.input_files): # Тут шедевроцикл где я прохожусь по файлам
        text = read_text(file_path, encoding=args.encoding)
        normal_text = normalize(text)
        tokens = tokenize(normal_text)
        words_cnt = count_freq(tokens)
        top_all_words = top_n(words_cnt, len(words_cnt))

        for word, count in top_all_words:
            per_file.append([file_path, word, count])

        for word, count in words_cnt.items():
            all_cnt[word] = all_cnt.get(word, 0) + count
    # endregion

    # region Итоговая запись
    s_cnt = top_n(all_cnt, len(all_cnt)) # Это чтобы отсортировать словарь
    write_csv(per_file, args.per_file, header=('file', 'word', 'count'))
    write_csv(list(s_cnt), args.total, header=('word', 'count'))

    total_words = sum(all_cnt.values())
    unique_words = len(s_cnt)

    print(f'Всего слов: {total_words} \n \nУникальных слов: {unique_words}')
    
    top5 = s_cnt[:5]
    if top5:
        max_len = max(max([len(word[0]) for word in top5]), len('слово'))
    else:
        max_len = len('слово')

    head = f'{"слово":<{max_len}} | частота'

    print(head)
    print('-' * len(head))
    for top in top5:
        print(f'{top[0]:<{max_len}} | {top[1]}')
    print('...')
    # endregion