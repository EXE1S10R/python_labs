import json
import csv
from pathlib import Path
from src.lib.often_func import ensure_parent_dir


def json_to_csv(json_path: str, csv_path: str) -> None:
    '''Записывает значения

    Args:
        json_path: Путь к json файлу из которого читаем
        csv_path: Путь к csv файлу куда пишем

    Returns: 
        None

    Raises:
        FileNotFoundError: 
            Указанный JSON файл не найден
        ValueError:
            Указанный файл не формата JSON
            Пустой JSON или неподдерживаемая структура
            Файл JSON пустой или имеет неправильный формат
            Все элементы списка JSON должны быть словарями
    '''
    jp = Path(json_path)
    cp = Path(csv_path)

    if not jp.exists():
        raise FileNotFoundError("Указанный JSON файл не найден")

    if jp.suffix.lower() != '.json':
        raise ValueError("Указанный файл не формата JSON")

    with jp.open('r', encoding='utf-8') as p:
        try:
            data = json.load(p)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError('Файл JSON пустой или имеет неправильный формат')
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы списка JSON должны быть словарями")

    ensure_parent_dir(cp)
    fieldnames = {}
    for element in data:
        for key in element.keys():
            fieldnames[key] = None

    with cp.open('w', newline="", encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames.keys()))
        w.writeheader()
        w.writerows(data)

# json_to_csv(r'data\lab05\samples\people.json', r'data\lab05\out\people_from_json.csv')


def csv_to_json(csv_path: str, json_path: str) -> None:
    '''Записывает значения

    Args:
        csv_path: Путь к csv файлу из которого читаем
        json_path: Путь к json файлу куда пишем

    Returns: 
        None

    Raises:
        FileNotFoundError: 
            Указанный CSV файл не найден
        ValueError:
            Указанный файл не формата CSV
            Файл CSV пустой
            Файл CSV не содержит данных
    '''
    jp = Path(json_path)
    cp = Path(csv_path)

    if not cp.exists():
        raise FileNotFoundError("Указанный CSV файл не найден")

    if cp.suffix.lower() != '.csv':
        raise ValueError("Указанный файл не формата CSV")

    with cp.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("Файл CSV пустой")

        data = list(reader)

    if not data:
        raise ValueError("Файл CSV не содержит данных")

    ensure_parent_dir(jp)
    with jp.open('w', encoding='utf-8') as p:
        json.dump(data, p, ensure_ascii=False, indent=2)

# csv_to_json(r'data\lab05\samples\people.csv', r'data\lab05\out\people_from_csv.json')


if __name__ == '__main__':
    csv_to_json(r'data\lab05\samples\people.csv',
                r'data\lab05\out\people_from_csv.json')
    json_to_csv(r'data\lab05\samples\people.json',
                r'data\lab05\out\people_from_json.csv')
