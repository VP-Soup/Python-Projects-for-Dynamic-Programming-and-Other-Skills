"""
The task is to find the length of the longest subsequence in a given array of integers such that all elements of the
subsequence are sorted in strictly ascending order. This is called the Longest Increasing Subsequence (LIS) problem.
"""


# FAILS -  space: O(n); time: O(nlogn)?
def longest_increasing_subsequence(array):
    list_ends = []
    max_length = 1
    for i in array:
        if not list_ends:
            list_ends.append([i, 1])
        elif i < list_ends[0][0]:
            list_ends.insert(0, [i, 1])
        elif i > list_ends[-1][0]:
            max_length += 1
            list_ends.append([i, max_length])
        else:
            j = len(list_ends) - 2
            while list_ends[j][0] >= i:
                j -= 1
            list_ends.insert(j + 1, [i, list_ends[j][1] + 1])
            print(list_ends)
            for k in range(len(list_ends) - 1, j + 1, -1):
                print(k)
                if list_ends[k][1] == list_ends[j + 1][1]:
                    list_ends.pop(k)
            max_length = max(max_length, list_ends[j + 1][1])
            print(list_ends)
    print(list_ends)
    return max_length


# print(longest_increasing_subsequence([5, 2, 7, 4, 3, 8]))
# print(longest_increasing_subsequence([6, 2, 4, 3, 7, 4, 5]))


# FAILS -  https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
# binary search function
def ceiling_index(array, l, r, key):
    while r - l > 1:
        m = l + (r - l) // 2
        if array[m] >= key:
            r = m
        else:
            l = m
    return r


def longest_increasing_subsequence2(array):
    size = len(array)
    if size == 0:
        return 0
    if size == 1:
        return 1
    tails = [0] * (size + 1)
    tails[0] = array[0]
    max_length = 1
    for i in range(1, size):
        print(tails)
        # case 1: array[i] is smallest end val
        if array[i] < tails[0]:
            tails[0] = array[i]
        # case 2: array[i] is the largest end val
        elif array[i] > tails[max_length - 1]:
            tails[max_length] = array[i]
            max_length += 1
        # case 3: array[i] is a middle value
        else:
            position = ceiling_index(tails, -1, max_length - 1, array[i])
            tails[position] = array[i]
    return max_length


# WORKS - https://www.geeksforgeeks.org/construction-of-longest-monotonically-increasing-subsequence-n-log-n/
def ceiling_index2(array, T, l, r, key):
    while r - l > 1:
        m = l + (r - l) // 2
        if array[T[m]] >= key:
            r = m
        else:
            l = m
    return r


def longest_increasing_subsequence3(array):
    size = len(array)
    if size == 0:
        return 0
    if size == 1:
        return 1
    tail_indices = [0] * (size + 1)
    prev_indices = [-1] * (size + 1)
    max_length = 1
    for i in range(1, size):
        print(tail_indices)
        # case 1: array[i] is smallest end val
        if array[i] < array[tail_indices[0]]:
            tail_indices[0] = i
        # case 2: array[i] is the largest end val
        elif array[i] > array[tail_indices[max_length - 1]]:
            prev_indices[i] = tail_indices[max_length - 1]
            tail_indices[max_length] = i
            max_length += 1
        # case 3: array[i] is a middle value
        else:
            position = ceiling_index2(array, tail_indices, -1, max_length - 1, array[i])
            prev_indices[i] = tail_indices[max_length - 1]
            tail_indices[position] = i
    # print LIS
    i = tail_indices[max_length - 1]
    while i >= 0:
        print(array[i], " ", end="")
        i = prev_indices[i]
    print()
    return max_length


print(longest_increasing_subsequence2([2, 7, 4, 3, 8]))
print(longest_increasing_subsequence3([2, 7, 4, 3, 8]))
# print(longest_increasing_subsequence3([2, 4, 3, 7, 4, 5]))
