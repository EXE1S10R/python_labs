# Отчет по лабораторной работе №3 — Тексты и частоты слов

## Задание A — Библиотечный модуль `src/lib/text.py`

Реализован переиспользуемый модуль `src/lib/text.py`, содержащий чистые функции для нормализации текста, токенизации, подсчета частоты слов и формирования топа слов.

### 1. Функция `normalize`
Преобразует строку: приведение к нижнему регистру (`casefold`), замена `ё/Ё` на `е/Е` и удаление управляющих символов и лишних пробелов.

```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''Нормализует текст

    Args:
        text: Исходный текст
        casefold: Переводить ли буквы в строчные (casefold)
        yo2e: Заменять ли ё/Ё на е/Е

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

```
![Выполнение кода](../../images/lab03/text(normalise).png)

*Рис. 1. Результат работы и тестов функции normalize*

---

### 2. Функция `tokenize`

Разбивает текст на слова (буквы, цифры, знак подчеркивания) по разделителям, сохраняя дефисы внутри слов.

```python
import re


def tokenize(text: str) -> list[str]:
    '''Разбивает текст на слова (токены)'''
    return [match.group() for match in re.finditer(r'\w+(-\w+)*', text)]

```

![Выполнение кода](../../images/lab03/text(tokenize).png)

*Рис. 2. Результат работы и тестов функции tokenize*

---

### 3. Функции `count_freq` и `top_n`

`count_freq` подсчитывает частоту встречаемости токенов за линейное время $O(N)$. `top_n` возвращает первые $N$ частых слов с алфавитной сортировкой при равенстве частот.

```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    '''Считает количество повторений токенов

    Args:
        tokens: Список слов (токенов)

    Returns:
        freq: Словарь: [слово] -> [количество повторений]
    '''
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    '''Выводит топ-N слов по частоте обращения

    Args:
        freq: Словарь с частотами слов
        n (=5): Количество элементов для топа

    Returns:
        Список кортежей (слово, количество повторений)
    '''
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]

```

![Выполнение кода](../../images/lab03/text(count_freq%20+%20top_n).png)

*Рис. 3. Результат работы и тестов функций count_freq и top_n*

---

## Задание B — Скрипт статистики `src/lab03/text_stats.py`

Скрипт читает вход из `stdin`, вызывает функции из `src/lib/text.py` и печатает базовую статистику текста.

### Исходный код `src/lab03/text_stats.py`

```python
from src.lib.text import normalize, tokenize, count_freq, top_n


text = open(0, encoding='utf-8').read()
if text.strip() == '':
    raise ValueError('Не был введен текст')

if_beautiful = 1  # Переменная, определяющая красивый (табличный) вывод


normal_text = normalize(text)
tokens = tokenize(normal_text)
words_cnt = count_freq(tokens)
top_words = top_n(words_cnt)


print(f'''
Всего слов: {len(tokens)}
Уникальных слов: {len(words_cnt)}
Топ-5:''')

if not if_beautiful:  # обычный вывод
    for tops in top_words:
        print(f'{tops[0]}:{tops[1]}')
else:  # Красивый вывод
    max_len = max([len(word[0]) for word in top_words] + [len('слово')])
    head = f'{"слово":<{max_len}} | частота'

    print(head)
    print('-' * len(head))
    for top in top_words:
        print(f'{top[0]:<{max_len}} | {top[1]}')
    print('...')

```

### Примеры работы скрипта

#### 1. Обычный режим вывода

![Выполнение кода](../../images/lab03/text_ststs(normal).png)

*Рис. 4. Результат запуска скрипта в обычном режиме*

#### 2. Табличный (красивый) режим вывода

![Выполнение кода](../../images/lab03/text_stats(beautiful).png)

*Рис. 5. Результат запуска скрипта в красивом табличном режиме*
