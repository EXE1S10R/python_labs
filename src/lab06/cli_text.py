import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description='CLI-утилиты для lab06')
    subparsers = parser.add_subparsers(dest='command')

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == 'cat':
        path = Path(args.input)

        if not path.exists():
                    raise FileNotFoundError(f'Нет файла по указанному пути: {path}')
                
        with open(path, 'r', newline='', encoding='utf-8') as f:
            data = f.readlines()

        if args.n:
            for i in range(len(data)):
                 print(f'{i+1:>4}\t{data[i]}', end='')
        else:
            for i in range(len(data)):
                 print(data[i], end='')

   
    elif args.command == 'stats':
        path = Path(args.input)

        if not path.exists():
            raise FileNotFoundError(f'Нет файла по указанному пути: {path}')
        
        with open(path, 'r', newline='', encoding='utf-8') as f:
            data = f.read()

        normal_text = normalize(data)
        tokens = tokenize(normal_text)
        words_cnt = count_freq(tokens)
        top_words = top_n(words_cnt, int(args.top))

        # Красивый вывод
        if top_words:
            max_len = max(max([len(word[0]) for word in top_words]), len('слово'))
        else:
            max_len = len('слово')
        head = f'{"слово":<{max_len}} | частота'

        print(head)
        print('-' * len(head))
        for top in top_words:
            print(f'{top[0]:<{max_len}} | {top[1]}')
        print('...')
        
        
        



if __name__ == '__main__':
    main()