from heapq import *

def ksort(numbers, k):
    heap = numbers[:k+1]
    heapify(heap)
    insert_index = 0
    for i in range(k+1, len(numbers)):
        numbers[insert_index] = heappop(heap)
        heappush(heap, numbers[i])
        insert_index += 1
    while heap:
        numbers[insert_index] = heappop(heap)
        insert_index += 1