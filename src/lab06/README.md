# Отчет по лабораторной работе №6 — CLI-утилиты с argparse (cat/stats + конвертеры)

## Цель работы

Создание консольных инструментов с аргументами командной строки, подкомандами и флагами с использованием модуля `argparse`. Обертка функций анализа текста из ЛР3 и конвертеров данных из ЛР5 в CLI-интерфейсы.

## 1. Текстовые CLI-утилиты (`src/lab06/cli_text.py`)

Модуль предоставляет подкоманды `cat` и `stats` для работы с текстовыми файлами.

### Подкоманда `cat`

Выводит содержимое файла в консоль. При вызове флага `-n` добавляется нумерация строк с правым выравниванием.

```bash
# Вывод без нумерации
python -m src.lab06.cli_text cat --input data/samples/people.csv

# Вывод с нумерацией строк
python -m src.lab06.cli_text cat --input data/samples/people.csv -n

Рис. 1. Вывод содержимого файла с нумерацией строк (cat -n).
Подкоманда stats

Выполняет нормализацию, токенизацию и подсчет частот слов с выводом таблицы Топ-N частых слов.
Bash

# Топ-5 слов по умолчанию
python -m src.lab06.cli_text stats --input data/samples/people.txt

# Задание собственного топа
python -m src.lab06.cli_text stats --input data/samples/people.txt --top 10

Рис. 2. Вывод частотного анализа текста (stats --top 10).
2. CLI-конвертеры данных (src/lab06/cli_convert.py)

Модуль предоставляет интерфейс для конвертации форматов JSON, CSV и XLSX.
Доступные подкоманды:

    json2csv — конвертация JSON в CSV.

    csv2json — конвертация CSV в JSON.

    csv2xlsx — конвертация CSV в XLSX.

Примеры вызова:
Bash

# JSON -> CSV
python -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people.csv

# CSV -> JSON
python -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people.json

# CSV -> XLSX
python -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx

Рис. 3. Результат работы CLI-конвертеров.
3. Справка и обработка ошибок

Каждая утилита поддерживает автоматическую генерацию встроенной справки по флагу --help:
Bash

python -m src.lab06.cli_text --help
python -m src.lab06.cli_text cat --help
python -m src.lab06.cli_convert --help

При отсутствии файла выбрасывается понятное исключение FileNotFoundError с указанием конкретного пути.
```
