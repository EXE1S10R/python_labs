import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort, merge_sort, counting_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def check_sorting(fn, trials: int = 100) -> None:
    '''Тестирование сортировок

    Args:
        fn: Функция сортировки
        trials: Количество проверок. Defaults: 10

    Returns:
        None

    Raises:
        AssertionError: '{fn.__name__} ошибся на {data}: {result}'
            Неправильная сортировка на примере data
        AssertionError: "{fn.__name__} изменила исходный список"
            Был изменен изначальный список    

    Prints:
        {Название сортировки} OK: {trials} проверок    
    '''

    for _ in range(trials):
        n = random.randint(0, 50)
        data = [random.randint(-100, 100) for _ in range(n)]
        original = list(data)
        result = fn(data)
        assert result == sorted(
            data), f'{fn.__name__} ошибся на {data}: {result}'
        assert data == original, f"{fn.__name__} изменила исходный список"

    print(f"{fn.__name__} OK: {trials}")


def check_search(trials: int = 100) -> None:
    '''Тестирование алгоритмов поиска

    Args:
        trials: Количество проверок. Defaults: 100

    Returns:
        None

    Raises:
        AssertionError: 'linear_search не нашел...' / 'binary_search не нашел...'
            Поиск вернул неверный индекс или не нашел существующий элемент
        AssertionError: '... нашел несуществующий элемент'
            Функция поиска нашла элемент, которого изначально не было в списке

    Prints:
        OK: {trials} проверок    
    '''
    for _ in range(trials):
        n = random.randint(0, 50)
        data = [random.randint(-100, 100) for _ in range(n)]
        random_number = random.randint(-100, 100)

        try:
            data.index(random_number)

            assert data[linear_search(
                data, random_number)] == random_number, "linear_search не нашел существующий случайный элемент"
            assert data[linear_search(
                data, data[0])] == data[0], "linear_search не нашел первый элемент"
            assert data[linear_search(
                data, data[-1])] == data[-1], "linear_search не нашел последний элемент"
            assert linear_search(data, 123456789) == - \
                1, "linear_search нашел несуществующий элемент"

            sort_data = sorted(data)

            assert sort_data[binary_search(
                sort_data, random_number)] == random_number, "binary_search не нашел существующий случайный элемент"
            assert sort_data[binary_search(
                sort_data, data[0])] == data[0], "binary_search не нашел первый элемент исходного списка"
            assert sort_data[binary_search(
                sort_data, data[-1])] == data[-1], "binary_search не нашел последний элемент исходного списка"
            assert binary_search(sort_data, 123456789) == - \
                1, "binary_search нашел несуществующий элемент"

        except ValueError:
            assert linear_search(data, random_number) == - \
                1, "linear_search нашел элемент, которого нет"

            sort_data = sorted(data)
            assert binary_search(sort_data, random_number) == - \
                1, "binary_search нашел элемент, которого нет"

    print(f"OK: {trials} проверок")


def check_two_sum(trials: int = 100) -> None:
    '''Тестирование алгоритмов поиска суммы двух элементов (two_sum)

    Args:
        trials: Количество проверок. Defaults: 100

    Returns:
        None

    Raises:
        AssertionError: 'brute_find не нашел, а fast_find нашел...' (или наоборот)
            Результаты алгоритмов разошлись: один нашел решение, а другой — нет
        AssertionError: '... вернул неверную сумму!'
            Сумма значений по найденным индексам не совпадает с искомым числом

    Prints:
        OK: {trials} проверок    
    '''
    for _ in range(trials):
        n = random.randint(0, 50)
        data = list(set([random.randint(-100, 100) for _ in range(n)]))
        random_number = random.randint(-100, 100)

        brute_find = two_sum_brute(data, random_number)
        fast_find = two_sum_fast(data, random_number)

        if brute_find is None:
            assert fast_find is None, f"brute_find не нашел, а fast_find нашел: {fast_find}"
        else:
            assert fast_find is not None, "brute_find нашел, а fast_find - нет"

            i, j = brute_find
            assert data[i] + \
                data[j] == random_number, "brute_find вернул неверную сумму!"

            i, j = fast_find
            assert data[i] + \
                data[j] == random_number, "fast_find вернул неверную сумму!"

    print(f"OK: {trials} проверок")


def check_counting_sort(trials: int = 100) -> None:
    '''Тестирование сортировки подсчетом ★ 

    Args:
        trials: Количество проверок. Defaults: 10

    Returns:
        None

    Raises:
        AssertionError: 'counting_sort ошибся на {data}: {result}'
            Неправильная сортировка на примере data
        AssertionError: "counting_sort изменила исходный список"
            Был изменен изначальный список    

    Prints:
        counting_sort OK: {trials} проверок    
    '''
    for _ in range(trials):
        n = random.randint(0, 50)
        lo, hi = -50, 50
        data = [random.randint(lo, hi) for _ in range(n)]
        original = list(data)

        result = counting_sort(data, lo, hi)

        assert result == sorted(
            data), f'counting_sort ошибся на {data}: {result}'
        assert data == original, "counting_sort изменила исходный список"

    print(f"counting_sort OK: {trials}")


if __name__ == "__main__":
    print()
    print("Проверка сортировок...")
    print()
    check_sorting(bubble_sort)
    check_sorting(insertion_sort)
    check_sorting(selection_sort)
    check_sorting(merge_sort)
    check_counting_sort()
    print("Сортировки в порядке >.<")
    print()

    print("-------------------------")
    print("Проверка поиска...")
    print()
    check_search()
    print("Поиск в порядке >.<")
    print()

    print("-------------------------")
    print("Проверка поиска суммы...")
    print()
    check_two_sum()
    print("Поиск суммы в порядке >.<")
    print()
    print("-------------------------")

    print("ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ!")
