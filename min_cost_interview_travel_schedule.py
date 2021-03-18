"""
A company wants to fly candidates for the interview. The company has two office locations,
one in Panama City with m and other in Tallahassee with n, where m is the maxmimum capacity
which Panama City office can take and n is the maximum capacity which Tallahassee office can take.

You are given the cost it incurs to fly in each candidate to ECP and TLH.

[500, 300],[540, 600],[550, 600],[300, 50]..so on

Write an algorithm for the minimum total cost?

"""

# no source -  time:O(t) space:O(t)
def minimum_cost_travel(pairs, m, n, t):
    if t > m + n:
        return 0
    min_cost = m_count = 0
    preference = []
    for c in range(len(pairs)):
        preference.append((pairs[c][0] - pairs[c][1], c))
    preference.sort()
    while m_count < m:
        temp1, temp2 = preference.pop(0)
        min_cost += pairs[temp2][0]
        m_count += 1
    while preference:
        temp1, temp2 = preference.pop(0)
        min_cost += pairs[temp2][1]
    return min_cost


array = [[100, 50], [200, 100], [70, 60], [80, 40]]
print(minimum_cost_travel(array, 2, 2, 4))
