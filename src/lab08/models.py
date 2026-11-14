from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")


def validate_student(rec: dict, *, today: str|None = None) -> None:
    '''Проверяет словарь с данными студента на корректность ключей и значений.

    Args:
        rec: Словарь с данными студента
        *today: Референсная дата для сравнения. Defaults: date.today()

    Returns:
        None

    Raises:
        ValueError: 
            Запись студента должна быть словарем
            Неверный набор ключей.
            Поле '{fio/group}' должно быть непустой строкой"
            Поле 'birthdate' должно быть строкой формата YYYY-MM-DD
            Поле 'birthdate' должно соответствовать формату YYYY-MM-DD
            Некорректная или несуществующая дата рождения: 
            Дата рождения ещё не наступила
            Поле 'gpa' должно быть int или float
            Поле 'gpa' должно быть в диапазоне от 0 до 5, получено: {gpa}
    '''
    if not isinstance(rec, dict):
        raise ValueError("Запись студента должна быть словарем")

    if set(rec.keys()) != set(STUDENT_FIELDS):
        raise ValueError(f"Неверный набор ключей.")

    for field in ("fio", "group"):
        val = rec[field]
        if not isinstance(val, str) or not val.strip():
            raise ValueError(f"Поле '{field}' должно быть непустой строкой")

    b_str = rec["birthdate"]
    if not isinstance(b_str, str):
        raise ValueError("Поле 'birthdate' должно быть строкой формата YYYY-MM-DD")

    if len(b_str) != 10 or b_str[4] != "-" or b_str[7] != "-":
        raise ValueError("Поле 'birthdate' должно соответствовать формату YYYY-MM-DD")

    try:
        b_date = date.fromisoformat(b_str)
    except ValueError:
        raise ValueError(f"Некорректная или несуществующая дата рождения: '{b_str}'")

    if today is None:
        ref_date = date.today()
    elif isinstance(today, str):
        try:
            ref_date = date.fromisoformat(today)
        except ValueError:
            raise ValueError(f"Некорректная или несуществующая дата референса: '{today}'")
    if b_date > ref_date:
        raise ValueError(f"Дата рождения ещё не наступила")

    gpa = rec["gpa"]
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise ValueError("Поле 'gpa' должно быть int или float")

    if not (0 <= gpa <= 5):
        raise ValueError(f"Поле 'gpa' должно быть в диапазоне от 0 до 5, получено: {gpa}")


def make_student(fio: str, birthdate: str, group: str, gpa: float | int) -> dict:
    '''Создание записи студента

    Args:
        fio: ФИО студента ⁡⁢⁣⁣!непустая строка!⁡
        birthdate: Дата рождения в формате YYYY-MM-DD
        group: Название группы ⁡⁢⁣⁡⁢⁣⁣!непустая строка!⁡
        gpa: Средний балл от 0 до 5

    Returns:
        rec: Словарь-запись студента

    Raises:
        ValueError: Неверные данные
    '''
    rec = {
        "fio": fio.strip() if isinstance(fio, str) else fio,
        "birthdate": birthdate,
        "group": group.strip() if isinstance(group, str) else group,
        "gpa": gpa,
    }
    validate_student(rec)
    rec["gpa"] = float(rec["gpa"])
    return rec


def student_age(rec: dict, today: date | None = None) -> int:
    '''Вычисление возраста студента

    Args:
        rec: Словарь с данными
        today: Дата, на которую считается возраст. Defaults: date.today()

    Returns:
        Полное количество лет

    Raises:
        ValueError: 
            Неверные данные записи
            Некорректная или несуществующая дата референса: '{b_str}'
            Дата рождения ещё не наступила
    '''
    validate_student(rec)
    b_date = date.fromisoformat(rec["birthdate"])

    if today is None:
        ref_date = date.today()
    elif isinstance(today, str):
        try:
            ref_date = date.fromisoformat(today)
        except ValueError:
            raise ValueError(f"Некорректная или несуществующая дата референса: '{today}'")
    else:
        ref_date = date.today()

    if b_date > ref_date:
        raise ValueError(f"Дата рождения ещё не наступила")

    had_birthday = (ref_date.month, ref_date.day) >= (b_date.month, b_date.day)
    return ref_date.year - b_date.year - (0 if had_birthday else 1)


def _age_word(age: int) -> str:
    '''Возвращает правильное склонение слова.
    Args:
        age: Количество дней

    Returns:
        Слово "год/года/лет"
    '''
    if 11 <= age % 100 <= 14:
        return "лет"
    if age % 10 == 1:
        return "год"
    if age % 10 in (2, 3, 4):
        return "года"
    return "лет"


def format_student(rec: dict) -> str:
    '''Форматирует запись студента в красивую строку:
        "Иванов И.И. (БИВТ-26-6-1), 19 лет, GPA 4.30"

    Args:
        rec: Словарь с данными

    Returns:
        Отформатированная строка

    Raises:
        ValueError: Неверные данные записи
    '''
    validate_student(rec)

    parts = rec["fio"].strip().split()
    if len(parts) >= 2:
        initials = "".join(f"{p[0].upper()}." for p in parts[1:])
        short_fio = f"{parts[0].capitalize()} {initials}"
    else:
        short_fio = parts[0].capitalize()

    age = student_age(rec)
    return f"{short_fio} ({rec['group'].strip().upper()}), {age} {_age_word(age)}, GPA {rec['gpa']:.2f}"


def student_to_dict(rec: dict) -> dict:
    '''Возвращает копию словаря студента для сериализации.

    Args:
        rec: Словарь с данными студента

    Returns:
        Новый словарь с полями STUDENT_FIELDS
    '''
    validate_student(rec)
    return {
        "fio": rec["fio"].strip(),
        "birthdate": rec["birthdate"],
        "group": rec["group"].strip(),
        "gpa": float(rec["gpa"]),
    }


def student_from_dict(d: dict) -> dict:
    '''Десериализайия словаря в запись студента.

    Args:
        d: Входной словарь

    Returns:
        Словарь-запись студента

    Raises:
        ValueError: 
            Входные данные должны быть словарем
            В словаре отсутствуют обязательные поля: {missing}
            Неверные данные записи
    '''
    if not isinstance(d, dict):
        raise ValueError("Входные данные должны быть словарем")

    missing = [k for k in STUDENT_FIELDS if k not in d]
    if missing:
        raise ValueError(f"В словаре отсутствуют обязательные поля: {missing}")

    return make_student(
        fio=d["fio"],
        birthdate=d["birthdate"],
        group=d["group"],
        gpa=d["gpa"],
    )