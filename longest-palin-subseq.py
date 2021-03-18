def longestPalSub(s):
    max_len = 1
    final_start = 0
    for i in range(1, len(s)):
        start = i - 1
        end = i
        while start >= 0 and end < len(s) and s[start] == s[end]:
            if end - start + 1 > max_len:
                final_start = start
                max_len = end - start + 1
            elif end - start + 1 == max_len:
                if s[start:end] > s[final_start:final_start+max_len]:
                    final_start = start
                    max_len = end - start + 1
            start -= 1
            end += 1

        start = i - 1
        end = i + 1
        while start >= 0 and end < len(s) and s[start] == s[end]:
            if end - start + 1 > max_len:
                final_start = start
                max_len = end - start + 1
            elif end - start + 1 == max_len:
                if s[start:end] > s[final_start:final_start + max_len]:
                    final_start = start
                    max_len = end - start + 1
            start -= 1
            end += 1
    return s[final_start:final_start+max_len]

s = 'bbeebeb'
print(longestPalSub(s))

# time: O(n^2)
# space: O(1)