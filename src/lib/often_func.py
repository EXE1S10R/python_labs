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
