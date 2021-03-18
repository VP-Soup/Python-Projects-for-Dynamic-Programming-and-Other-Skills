# time: O(m*n), space: O(n)
def maxNumChanges(n, coins):
    # holds ways to make change for all values 0 to n
    changes = [0 for i in range(n+1)]
    # 1 way to calculate n = 0
    changes[0] = 1
    for i in coins:
        for j in range(n+1):
            # if the coin value is larger than the desired n, add ways to make that value without the coin
            if j >= i:
                changes[j] += changes[j-i]
    return changes[n]