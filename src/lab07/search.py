def linear_search(nums: list, x: int) -> int:
    '''Линейная сортировка

    Args:
        nums: Список с набором чисел
        x: Искомое число

    Returns:
        i: Искомый индекс элемента списка (-1 если элемент отсутствует)

    Complexity:
        O(n): Линейная сложность
    '''
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


def binary_search(sorted_nums: list, x: int) -> int:
    '''Бинарный поиск

    Args:
        sorted_nums: Список чисел ⁡⁢⁣⁣!отсортированный!⁡
        x: Искомое число

    Returns:
        i: Искомый индекс элемента списка (-1 если элемент отсутствует)

    Complexity:
        O(log n): Логарифмическая сложность
    '''
    lo = 0
    hi = len(sorted_nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def two_sum_brute(nums: list, target: int) -> tuple[int, int] | None:
    '''Поиск двух элементов с искомой суммой (долгий вложенный цикл)

    Args:
        nums: Список чисел ⁡⁢⁣⁣!нет повторяющихся элементов!⁡
        target: Искомая сумма

    Returns:
        (i, j): Числа сумма которых равна target (i < j)
        None: Нет нужных чисел

    Complexity:
        O(n**2): Квадратичная сложность
    '''
    for i in nums:
        for j in nums:
            if i != j and i + j == target:
                return (min(i, j), max(i, j))


def two_sum_fast(nums: list, target: int) -> tuple[int, int] | None:
    '''Поиск двух элементов с искомой суммой (быстрый словарь)

    Args:
        nums: Список чисел ⁡⁢⁣⁣!нет повторяющихся элементов!⁡
        target: Искомая сумма

    Returns:
        (i, j): Числа сумма которых равна target (i < j)
        None: Нет нужных чисел

    Complexity:
        O(n): Линейная сложность
    '''
    past = {}
    for i in range(len(nums)):
        x = nums[i]
        find = target - x
        if find in past:
            return (min(find, x), max(find, x))
        else:
            past[x] = i
