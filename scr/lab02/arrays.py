def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    ''' Вычисляет максимум и минимум списка

    Args: 
        nums: Список чисел (целых и вещественных)

    Returns:
        Кортеж (минимум, максимум)

    Raises:
        ValueError: Если список пустой
    '''
    if not (len(nums)):
        raise ValueError
    return (min(nums), max(nums))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    '''Возвращает отсортированный список

    Args:
        nums: Список чисел (целых и вещественных)

    Returns:
        Отсортированный список
    '''
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    '''Переводит матрицу в вектор

    Args:
        mat: Список в котором содержатся списки или кортежи
    
    Returns:
        vector: Список
    
    Raises:
        TypeError: Если передана не матрица
    '''
    vector = []
    for row in mat:
        if type(row) != list and type(row) != tuple:
            raise TypeError
        vector.extend(row)
    return vector


print('Тест кейсы:')
print()
print('min_max')
print(f'[3, -1, 5, 5, 0] -> {min_max([3, -1, 5, 5, 0])}')
print(f'[42] -> {min_max([42])}')
print(f'[-5, -2, -9] -> {min_max([-5, -2, -9])}')
print(f'[1.5, 2, 2.0, -3.1] -> {min_max([1.5, 2, 2.0, -3.1])}')
print(f'[] -> {min_max([])}')

