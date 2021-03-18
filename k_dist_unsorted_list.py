import math
import sys
from queue import *

def Kclosest(numbers, x, k):
    temp = PriorityQueue()
    for i in range(k):
        temp.put((-abs(numbers[i]-x), i))
    for i in range(k, len(numbers)):
        difference = abs(numbers[i] - x)
        temp_val, temp_index = temp.get()
        test = temp_val * -1
        if difference > test:
            temp.put((-test, temp_index))
            continue
        else:
            temp.put((-difference, i))
    result = []
    while not temp.empty():
        temp_val, temp_index = temp.get()
        result.append(numbers[temp_index])
    result.sort()
    return result


if __name__=='__main__':
    arr = [-10,-50,20,17,80]
    x,k = 20,2
    print(Kclosest(arr, x, k))
