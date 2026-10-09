from pathlib import Path


def is_matrix_full(mat: list[list]) -> bool:
    '''Проверяет не рваная ли матрица

    Args:
        mat: Матрица (список списков)

    Returns:
        True: Матрица равномерная
        False: Матрица рваная
    '''
    n, m = len(mat), len(mat[0])

    for i in range(n):
        if len(mat[i]) != m:
            return False
    return True


def ensure_parent_dir(path: str | Path) -> None:
    '''Проверяет наличие родительских папок, если их нет, то создает их
    Args:
        path: Путь к файлу в формате строки или Path

    Returns:
        None
    '''

    Path(path).parent.mkdir(parents=True, exist_ok=True)
