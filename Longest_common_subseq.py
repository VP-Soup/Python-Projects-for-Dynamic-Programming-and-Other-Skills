"""
A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the
order of the remaining elements. Longest common subsequence (LCS) of 2 sequences is a subsequence, with maximal length,
which is common to both the sequences.

Given two sequences of integers,  and , find the longest common subsequence and print it as a line of space-separated
integers. If there are multiple common subsequences with the same maximum length, print any one of them.

In case multiple solutions exist, print any of them. It is guaranteed that at least one non-empty common subsequence
will exist.

brute force:
O(2^m * n)
check all subsequences of 1 and check if it exists in 2

"""

# time and space: O(mn) - note possible to do in O(min(m,n)) space
def longest_common_subsequence(a, b):
    dp = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]
    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            if a[j - 1] == b[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    for i in dp:
        print(i)
    lcs_1 = []
    i = len(b)
    j = len(a)
    while i > 0 and j > 0:
        if a[j - 1] == b[i - 1]:
            lcs_1.insert(0, a[j - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return lcs_1


print(longest_common_subsequence("12341", "341213"))
