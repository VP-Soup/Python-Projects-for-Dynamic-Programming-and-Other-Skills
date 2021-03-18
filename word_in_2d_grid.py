"""
    Given a 2D board and a word, find if the word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cell,
    where "adjacent" cells are those horizontally or vertically neighboring.
    The same letter cell may not be used more than once.

    solution: https://www.geeksforgeeks.org/check-if-a-word-exists-in-a-grid-or-not/

"""

def exist(board, row, col, word):
    visited = []
    flag = []

    def search(t_row, t_col, word_index):
        if word_index == len(word):
            flag.append(1)
            return True
        if (t_row, t_col) in visited:
            return False

        if board[t_row][t_col] == word[word_index]:
            visited.append((t_row, t_col))
            if t_row > 0:
                search(t_row - 1, t_col, word_index + 1)
            if t_row < row - 1:
                search(t_row + 1, t_col, word_index + 1)
            if t_col > 0:
                search(t_row, t_col - 1, word_index + 1)
            if t_col < col - 1:
                search(t_row, t_col + 1, word_index + 1)
            visited.remove((t_row, t_col))
        return False

    for r in range(row):
        for c in range(col):
            search(r, c, 0)
            if flag:
                return True
    return False

# trie data structure - constructive tree from root t -> to -> tow -> etc.