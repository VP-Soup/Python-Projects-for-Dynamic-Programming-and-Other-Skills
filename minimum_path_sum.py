"""
Given a [m x n] integer grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
You can only move either "down" or "right" at any given point of time.

solution: https://www.geeksforgeeks.org/min-cost-path-dp-6/
"""

# O(r*c)
def minimum_path_sum(board, row, col):
    temp = [[0 for j in range(col)] for i in range(row)]
    temp[0][0] = board[0][0]
    for i in range(1, row):
        temp[i][0] = temp[i - 1][0] + board[i][0]
    for i in range(1, col):
        temp[0][i] = temp[0][i - 1] + board[0][i]
    for i in range(1, row):
        for j in range(1, col):
            temp[i][j] = min(temp[i-1][j], temp[i][j-1]) + board[i][j]
    return temp[row-1][col-1]
