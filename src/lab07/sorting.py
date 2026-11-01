def bubble_sort(nums: list[int]) -> list[int]:
    ''' Оптимизированная сортировка пузырьком
        есть ранний выход при отсортированном списке

    Args:
        nums: Список чисел

    Returns:
        arr: Отсортированный список чисел

    Complexity:
        O(n**2): Квадратичная сложность
    '''
    arr = list(nums)
    n = len(arr)

    for i in range(n):
        flag = 0
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1

        if not (flag):
            break

    return arr


def selection_sort(nums: list[int]) -> list[int]:
    ''' Сортировка выбором

    Args:
        nums: Список чисел

    Returns:
        arr: Отсортированный список чисел

    Complexity:
        O(n**2): Квадратичная сложность
    '''
    arr = list(nums)
    n = len(arr)

    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j

        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr


def insertion_sort(nums: list[int]) -> list[int]:
    '''Сортировка вставками

    Args:
        nums: Список чисел

    Returns:
        arr: Отсортированный список чисел

    Complexity:
        O(n**2): Квадратичная сложность
    '''
    arr = list(nums)
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
