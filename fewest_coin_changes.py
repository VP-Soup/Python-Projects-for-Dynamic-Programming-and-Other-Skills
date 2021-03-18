"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that there is no duplicates in the list of coins and you have an infinite number of each kind of coin.
"""

# NOTE: Failed Solution. 

# time O(n), n = len(coins); space O(1)
# note - if not given sorted coin list - need to sort making time O(nlogn)
# note - need to add catch '0' value coin edge case
def minimum_num_coin_changes(amount, coins):
    temp = amount
    changes = 0
    for i in range(len(coins) - 1, -1, -1):
        if temp != temp % coins[i]:
            temp = temp % coins[i]
            changes += 1
    if temp != 0:
        return -1
    return changes


print(minimum_num_coin_changes(5, [5, 6, 7, 9]))
