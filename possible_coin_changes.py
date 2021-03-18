"""
Given a value N, and we have infinite supply of each S = {S1, S2, S3, ..., Sm} valued coins,
how many ways can we make the change for N? The order of coins doesn't matter.
"""

# time: O(m*n), space: O(n)
def max_num_changes(amount, coins):
    # check if possible
    temp = amount
    for i in range(len(coins)):
        if temp == 0:
            break
        if temp != temp % coins[i]:
            temp = temp % coins[i]
    # if not possible return failure
    if temp != 0:
        return -1
    # calculate as usual
    changes = [0 for i in range(amount + 1)]
    changes[0] = 1
    for i in coins:
        for j in range(len(changes)):
            if j >= i:
                changes[j] += changes[j - i]
    return changes[amount]
