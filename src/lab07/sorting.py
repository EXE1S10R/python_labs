def bubble_sort(nums: list[int]) -> list[int]:
    ''' Оптимизированная сортировка пузырьком
        ★ есть ранний выход при отсортированном списке

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


def merge_sort(nums: list[int]) -> list[int]:
    '''★ Сортировка слиянием (без рекурсии)

    Args:
        nums: Список чисел

    Returns:
        arr: Отсортированный список чисел

    Complexity:
        O(n log n): Линейно-логарифмическая сложность
    '''
    arr = list(nums)
    n = len(arr)
    step = 1

    while step < n:
        for left in range(0, n, 2 * step):
            mid = left + step
            right = min(left + 2 * step, n)

            if mid >= n:
                continue

            merged = []
            i, j = left, mid

            while i < mid and j < right:
                if arr[i] <= arr[j]:
                    merged.append(arr[i])
                    i += 1
                else:
                    merged.append(arr[j])
                    j += 1

            while i < mid:
                merged.append(arr[i])
                i += 1
            while j < right:
                merged.append(arr[j])
                j += 1

            arr[left:right] = merged

        step *= 2

    return arr


def counting_sort(nums: list[int], lo: int, hi: int) -> list[int]:
    '''★ Сортировка подсчетом для целых чисел в диапазоне [lo, hi]

    Args:
        nums: Список чисел
        lo: Минимально возможное значение
        hi: Максимально возможное значение

    Returns:
        res: Отсортированный список чисел

    Complexity:
        O(n + k): Линейная сложность, k = (hi - lo)
    '''
    count = [0] * (hi - lo + 1)

    for x in nums:
        count[x - lo] += 1

    res = []
    for i in range(len(count)):
        res.extend([lo + i] * count[i])

    return res
