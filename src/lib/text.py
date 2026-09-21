import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''Нормализует текст

    Args:
        text: Исходный текст
        casefold: Bool значение
                    True: Переводит все буквы в строчные
                    False: Оставляет всё как есть
        yo2e: Заменяет ё/Ё на е/Е

    Returns:
        new_text: Итоговый обработанный текст
    '''
    new_text = text
    if casefold:
        new_text = new_text.casefold()
    if yo2e:
        new_text = new_text.replace('ё', 'е').replace('Ё', 'Е')
    new_text = ' '.join(new_text.split())
    return new_text


def tokenize(text: str) -> list[str]:
    return [match.group() for match in re.finditer(r'\w+(-\w+)*', text)]


def count_freq(tokens: list[str]) -> dict[str, int]:
    '''Считает количество повторений токенов

    Args:
        tokens: Список слов (токенов)

    Returns:
        freq: Словарь: [слово], [количество повторений]
    '''
    freq = {}
    for el in set(tokens):
        freq[el] = tokens.count(el)
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    '''Выводит топ n слов по частоте обращения

    Args:
        freq: Словарь где указаны слова и количество их повторений
        n (=5): Количество элементов которые нужно указать в топе

    Returns:  Список где находятся кортежи (слово, количество повторений)
    '''
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]


print('Тест кейсы:')

print(fr'''
normalize

"ПрИвЕт\nМИр\t" -> {normalize("ПрИвЕт\nМИр\t")}
"ёжик, Ёлка" -> {normalize("ёжик, Ёлка")}
"Hello\r\nWorld" -> {normalize("Hello\r\nWorld")}
"  двойные   пробелы  " -> {normalize("  двойные   пробелы  ")}
''')

print(fr'''
tokenize

"привет мир" -> {tokenize("привет мир")}
"hello,world!!!" -> {tokenize("hello,world!!!")}
"по-настоящему круто" -> {tokenize("по-настоящему круто")}
"2025 год" -> {tokenize("2025 год")}
"emoji 😀 не слово" -> {tokenize("emoji 😀 не слово")}
''')

print(fr'''
count_freq + top_n

Токены ["a","b","a","c","b","a"] -> частоты {count_freq(["a", "b", "a", "c", "b", "a"])};
top_n(..., n=2) -> {top_n(count_freq(["a", "b", "a", "c", "b", "a"]), 2)}

При равенстве частот: токены ["bb","aa","bb","aa","cc"] -> {count_freq(["bb", "aa", "bb", "aa", "cc"])};
top_n(..., n=2) → {top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), 2)}
''')
