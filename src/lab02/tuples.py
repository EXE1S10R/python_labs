def format_record(rec: tuple[str, str, float]) -> str:
    '''Функция форматирует запись, приводя ее в вид
       Иванов И.И., гр. BIVT-25, GPA 4.60

    Args:
        rec: Кортеж в котором содержится ФИО, группа и оценка

    Returns:
        Строку, где указано имя, инициалы, группа и оценка

    Raises:
        TypeError:
            'Запись должна быть кортежем'
            'Имя должно быть строкой'
            'Группа должна быть строкой'
            'Оценка должна быть вещественным числом'
        ValueError:
            'В кортеже должно быть 3 элемента'
            'Ведено не полное ФИО'
            'Группа не может быть пустой'
    '''

    name = []
    first_flag = 0

    # region Вызовы ошибок

    if len(rec) != 3:
        raise ValueError('В кортеже должно быть 3 элемента')
    if len(rec[0].strip().split()) != 3 and len(rec[0].strip().split()) != 2:
        raise ValueError('Ведено не полное ФИО')
    if not len(rec[1].strip()):
        raise ValueError('Группа не может быть пустой')

    if not isinstance(rec, tuple):
        raise TypeError('Запись должна быть кортежем')
    if not isinstance(rec[0], str):
        raise TypeError('Имя должно быть строкой')
    if not isinstance(rec[1], str):
        raise TypeError('Группа должна быть строкой')
    if not isinstance(rec[2], (float, int)):
        raise TypeError('Оценка должна быть вещественным числом')
    # endregion

    for word in rec[0].strip('" ').split():
        word = word.strip()
        if len(word) and first_flag:
            name.append(word[0].capitalize() + '.')
            first_flag = 1

        if len(word) and not (first_flag):
            name.append(word[0].capitalize() + word[1:] + ' ')
            first_flag = 1

    return f"{''.join(name)}, гр. {rec[1]}, GPA {rec[2]:.2f}"


print(f'''
Тест кейсы:
("Иванов Иван Иванович", "BIVT-25", 4.6) -> {format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}
("Петров Пётр", "IKBO-12", 5.0) -> {format_record(("Петров Пётр", "IKBO-12", 5.0))}
("Петров Пётр Петрович", "IKBO-12", 5.0) -> {format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))}
("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -> {format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}
''')

# Вызывает ошибку ValueError
# print(f'("Иванов Иван Иванович", "     ", 4.6) -> {format_record(("Иванов Иван Иванович", "    ", 4.1))}')
