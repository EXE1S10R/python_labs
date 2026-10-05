from pathlib import Path
import csv


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''Считывает текст по указанному пути

    Args:
        path: Путь к файлу в формате строки или Path
        encoding: Тип кодировки файла (пример: encoding="cp1251"), по умолчанию utf-8

    Returns:
        Прочитанный файл в виде строки
    '''

    return Path(path).read_text(encoding=encoding)


def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    '''Записывает частоты слов в csv файл
    Args:
        rows: Список строк которые нужно внести в файл
        path: Путь к файлу записи
        header: Заголовок файла
    
    Returns:
        None
    
    Raises:
        ValueError: Строки разной длинны
    '''
    
    etalon = len(rows[0])
    for r in rows:
        if len(r) != etalon:
            raise ValueError('Строки разной длинны')
    ensure_parent_dir(path)
    with Path(path).open('w', newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header:
            w.writerow(header)
        for row in rows:
            w.writerow(row)


def ensure_parent_dir(path: str | Path) -> None:
    '''Проверяет наличие родительских папок, если их нет, то создает их
    Args:
        path: Путь к файлу в формате строки или Path

    Returns:
        None
    '''

    Path(path).parent.mkdir(parents=True, exist_ok=True)
