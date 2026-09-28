from pathlib import Path

def read_text(path: str | Path, encoding: str = 'utf-8') -> str:
    '''Считывает текст по указанному пути

    Args:
        path: Путь к файлу в формате строки или Path
        encoding: Тип кодировки файла (пример: encoding="cp1251"), по умолчанию utf-8
    
    Returns:
        Прочитанный файл в виде строки

    Raises:

    '''
    with open(path, encoding=encoding) as file:
        return file.read()
