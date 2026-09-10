import heapq

def heap_sort(arr):
    heap = arr[:]
    heapq.heapify(heap)

    sorted_arr = []

    while heap:
        sorted_arr.append(heapq.heappop(heap))

    return sorted_arr