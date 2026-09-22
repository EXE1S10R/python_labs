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
        raise ValueError ('пустой список')
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
            raise TypeError ('Передана не матрица')
        vector.extend(row)
    return vector


print('Тест кейсы:')
print(f'''
min_max

[3, -1, 5, 5, 0] -> {min_max([3, -1, 5, 5, 0])}
[42] -> {min_max([42])}
[-5, -2, -9] -> {min_max([-5, -2, -9])}
[1.5, 2, 2.0, -3.1] -> {min_max([1.5, 2, 2.0, -3.1])}
''')
# Тест кейс который выводит ошибку ValueError
# print(f'[] -> {min_max([])}')

print(f'''
unique_sorted

[3, 1, 2, 1, 3] -> {unique_sorted([3, 1, 2, 1, 3])}
[] -> {unique_sorted([])}
[-1, -1, 0, 2, 2] -> {unique_sorted([-1, -1, 0, 2, 2])}
[1.0, 1, 2.5, 2.5, 0] -> {unique_sorted([1.0, 1, 2.5, 2.5, 0])}
''')

print(f'''
flatten

[[1, 2], [3, 4]] -> {flatten([[1, 2], [3, 4]])}
[[1, 2], (3, 4, 5)] -> {flatten([[1, 2], (3, 4, 5)])}
[[1], [], [2, 3]] -> {flatten([[1], [], [2, 3]])}''')

# Тест кейс который выводит ошибку TypeError
# print(f'[[1, 2], "ab"] -> {flatten([[1, 2], "ab"])}') 


