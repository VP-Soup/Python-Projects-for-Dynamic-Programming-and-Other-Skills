"""
https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
"""

# time: O(n) or O(nlogn)? space:O(n)?
def min_rooms(intervals):
    start = []
    end = []
    for i in intervals:
        start.append(i[0])
        end.append(i[1])
    start.sort()
    end.sort()
    rooms = result = s_index = 1
    e_index = 0
    while s_index < len(intervals) and e_index < len(intervals):
        if start[s_index] <= end[e_index]:
            rooms += 1
            s_index += 1
        else:
            rooms -= 1
            e_index += 1
        if rooms > result:
            result = rooms
    return result

array = [[0, 30], [5, 10], [25, 35]]
print(min_rooms(array))
