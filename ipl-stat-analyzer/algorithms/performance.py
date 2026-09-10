import random
import time

from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort


def compare_algorithms(size=1000):

    data = random.sample(range(size*10), size)

    results = {}

    start = time.perf_counter()
    merge_sort(data.copy())
    results["Merge Sort"] = time.perf_counter() - start

    start = time.perf_counter()
    quick_sort(data.copy())
    results["Quick Sort"] = time.perf_counter() - start

    start = time.perf_counter()
    heap_sort(data.copy())
    results["Heap Sort"] = time.perf_counter() - start

    return results