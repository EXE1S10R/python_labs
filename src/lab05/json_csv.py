import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    data = json.load(open(Path(json_path)))
    fieldnames = list(data[0].keys())

    with Path(csv_path).open('w', newline="", encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(data)

# json_to_csv(r'data\lab05\samples\people.json', r'data\lab05\out\people_from_json.csv')
def csv_to_json(csv_path: str, json_path:str) -> None:
    with Path(csv_path).open('r', newline="", encoding='utf-8') as f:
        with Path(json_path).open('w', newline="", encoding='utf-8') as p:
            data = list(csv.DictReader(f))
            json.dump(data, p, ensure_ascii=False, indent=2)

# csv_to_json(r'data\lab05\samples\people.csv', r'data\lab05\out\people_from_csv.json')