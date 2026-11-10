import csv
import timeit
import random
from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast



def bench_sorts(n: int) -> list[tuple]:
    data = [random.randint(-10000, 10000) for _ in range(n)]
    rows = []

    t_sorted = min(timeit.repeat(lambda: sorted(data), number=100, repeat=5)) / 100
    rows.append(("sort", n, "sorted", t_sorted))

    if n >= 100000:
        rows.append(("sort", n, "bubble_sort", "> 60.0"))
        rows.append(("sort", n, "insertion_sort", "> 60.0"))
        rows.append(("sort", n, "selection_sort", "> 60.0"))

    else:
        t_bubble = min(timeit.repeat(lambda: bubble_sort(data), number=1, repeat=5))
        rows.append(("sort", n, "bubble_sort", t_bubble))

        t_insertion = min(timeit.repeat(lambda: insertion_sort(data), number=1, repeat = 5))
        rows.append(("sort", n, "insertion_sort", t_insertion))

        t_selection = min(timeit.repeat(lambda: selection_sort(data), number=1, repeat=5))
        rows.append(("sort", n, "selection_sort", t_selection))

    return rows

def bench_search() -> list[tuple]:
    n = 100000
    queries_count = 10000

    data = [random.randint(-100000, 100000) for _ in range(n)]
    queries = [random.randint(-100000, 100000) for _ in range(queries_count)]
    rows = []

    def linear_runner():
        for q in queries:
            linear_search(data, q)

    t_linear = timeit.timeit(linear_runner, number=1)
    rows.append(("search", n, "linear", t_linear))

    t_sort = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("search", n, "sort_only", t_sort))
    sort_data = sorted(data)

    def binary_runner():
        for q in queries:
            binary_search(sort_data, q)

    t_binary = timeit.timeit(binary_runner, number=10) / 10
    rows.append(("search", n, "binary", t_binary))

    return rows


if __name__ == "__main__":
    random.seed(42)
    results = bench_sorts(1000)
    for r in results:
        print(r)
