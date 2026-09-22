from src.lib.often_func import is_matrix_full


def transpose(mat: list[list[float | int]]) -> list[list]:
    '''Меняет строки и столбцы местами

    Args:
        mat: Матрица

    Returns:
        trans: Транспонированная матрица

    Raises:
        ValueError: Строки разной длины
    '''
    if not(len(mat)):
        return []
    
    if not (is_matrix_full(mat)):
        raise ValueError('строки матрицы разной длины')

    n, m = len(mat), len(mat[0])
    trans = []
    for _ in range(m):
        trans.append([0] * n)

    for i in range(n):
        for j in range(m):
            trans[j][i] = mat[i][j]

    return trans


def row_sums(mat: list[list[float | int]]) -> list[float]:
    '''Сумма по каждой строке

    Args: 
        mat: Матрица чисел

    Returns:
        Список сумм по строке

    Raises:
        ValueError: Строки разной длины
    '''
    if not (is_matrix_full(mat)):
        raise ValueError('строки матрицы разной длины')
    return [sum(row) for row in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    '''Сумма по каждому столбцу

    Args:
        mat: Матрица чисел

    Returns:
        Список сумм по столбцам

    Raises:
        ValueError: Строки разной длины
    '''
    return [sum(row) for row in transpose(mat)]


print('Тест кейсы:')
print(f'''
transpose

[[1, 2, 3]] -> {transpose([[1, 2, 3]])}
[[1], [2], [3]] -> {transpose([[1], [2], [3]])}
[[1, 2], [3, 4]] -> {transpose([[1, 2], [3, 4]])}
[] -> {transpose([])}
''')

# Возвращает ошибку ValueError
# print(f'[[1, 2], [3]] -> {transpose([[1, 2], [3]])}')


print(f'''
row_sums

[[1, 2, 3], [4, 5, 6]] -> {row_sums([[1, 2, 3], [4, 5, 6]])}
[[-1, 1], [10, -10]] -> {row_sums([[-1, 1], [10, -10]])}
[[0, 0], [0, 0]] -> {row_sums([[0, 0], [0, 0]])}
''')

# Возвращает ошибку ValueError
# print(f'[[1, 2], [3]] -> {row_sums([[1, 2], [3]])}')


print(f'''
col_sums

[[1, 2, 3], [4, 5, 6]] → {col_sums([[1, 2, 3], [4, 5, 6]])}
[[-1, 1], [10, -10]] → {col_sums([[-1, 1], [10, -10]])}
[[0, 0], [0, 0]] → {col_sums([[0, 0], [0, 0]])}
''')

# Возвращает ошибку ValueError
# print(f'[[1, 2], [3]] -> {col_sums([[1, 2], [3]])}')