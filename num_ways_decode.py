"""
A message containing letters from A-Z is being encoded to numbers using the following: mapping:

'A' -> 1
'B' -> 2
 ...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/
"""

# time: O(n) space: O(n)
def num_ways_decode(word):
    ways = [0] * (len(word)+1)
    ways[0] = ways[1] = 1
    for i in range(2, len(word) + 1):
        ways[i] = 0
        if int(word[i - 1]) > 0:
            ways[i] = ways[i-1]
        if int(word[i-2]) == 1 or (int(word[i-2]) == 2 and int(word[i-1]) < 7):
            ways[i] += ways[i-2]
        print(ways)
    print(ways)
    return ways[len(word)]


print(num_ways_decode('12'))
print(num_ways_decode('122'))
print(num_ways_decode('1202'))

