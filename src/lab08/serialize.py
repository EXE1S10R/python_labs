import json
from pathlib import Path
from src.lab08.models import student_from_dict, student_to_dict
from src.lab04.io_txt_csv import ensure_parent_dir


def students_to_json(students: list[dict], path: str | Path) -> None:
    '''Список записей студентов в JSON-файл.

    Args:
        students: Список словарей с данными
        path: Путь к выходному JSON-файлу

    Returns:
        None

    Raises:
        ValueError:
            Ожидался список записей студентов
            Ошибка при записи №{i + 1}: {e}
    '''
    if not isinstance(students, (list, tuple)):
        raise ValueError("Ожидался список записей студентов")

    data = []
    for i, student in enumerate(students):
        try:
            data.append(student_to_dict(student))
        except ValueError as e:
            raise ValueError(f"Ошибка при записи №{i + 1}: {e}") from e

    file_path = Path(path)
    ensure_parent_dir(path)

    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> list[dict]:
    '''Загружает и валидирует список студентов из JSON-файла (политика strict).

    Args:
        path: Путь к входному JSON-файлу

    Returns:
        Список словарей-записей студентов

    Raises:
        FileNotFoundError: Файл не найден
        ValueError:
            Ошибка при записи №{i + 1}: {e}
            JSON должен быть списком
    '''
    file_path = Path(path)

    with file_path.open("r", encoding="utf-8") as f:
        raw_data = json.load(f)

    if not isinstance(raw_data, list):
        raise ValueError("JSON должен быть списком")

    students = []
    for i, item in enumerate(raw_data):
        try:
            students.append(student_from_dict(item))
        except ValueError as e:
            raise ValueError(f"Ошибка при записи №{i + 1}: {e}") from e

    return students