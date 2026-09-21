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
        new_text.replace('ё', 'е').replace('Ё', 'Е')
    new_text = ' '.join(new_text.split())
    return new_text

def tokenize(text: str) -> list[str]:
    return [match.group() for match in re.finditer(r'\w+(-\w+)*', text)]