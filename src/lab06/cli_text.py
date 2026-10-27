import argparse

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

    elif args.command == 'stats':




if __name__ == '__main__':
    main()