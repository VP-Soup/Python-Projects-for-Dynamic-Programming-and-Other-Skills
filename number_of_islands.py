"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
The input to this program is as follows. The first line contains the number of rows and number of columns.
Then, the actual grid configuration follows.

"""


def num_islands(grid, row, col):
    def check_island(target_row, target_column):
        if grid[target_row][target_column] == '1':
            grid[target_row][target_column] = '0'
            # check up
            if target_row > 0:
                check_island(target_row - 1, target_column)
                # check up right
                if target_column < col - 1:
                    check_island(target_row - 1, target_column + 1)
                # check up left
                if target_column > 0:
                    check_island(target_row - 1, target_column - 1)
            # check down
            if target_row < row - 1:
                check_island(target_row + 1, target_column)
                # check down right
                if target_column < col - 1:
                    check_island(target_row + 1, target_column + 1)
                # check down left
                if target_column > 0:
                    check_island(target_row + 1, target_column - 1)
            # check right
            if target_column < col - 1:
                check_island(target_row, target_column + 1)
            # check left
            if target_column > 0:
                check_island(target_row, target_column - 1)
            return 1
        return 0

    islands_found = 0
    for x in range(row):
        for y in range(col):
            if check_island(x, y) == 1:
                islands_found += 1
    return islands_found


