def palindrome(s):

    array = [[0 for i in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        array[i][i] = 1
    for i in range(len(s), -1, -1):
        for j in range(len(s)):
            if j > i:
                if s[i] == s[j] and i < len(s)-1 and j > 0:
                    array[i][j] = array[i+1][j-1] + 2
                else:
                    array[i][j] = max(array[i+1][j], array[i][j-1])
    i = 0
    j = len(s) -1
    pal = ''
    counter = 0
    while j > i:
        if s[i] == s[j]:
            pal += s[j]
            i += 1
            j -= 1
        elif array[i+1][j] > array[i][j-1]:
            i += 1
        elif array[i + 1][j] < array[i][j - 1]:
            j -= 1
        elif s[i+1] < s[j-1]:
            i += 1
        else:
            j -= 1

    print(array[0][len(s) - 1])
    if array[0][len(s) - 1]%2 == 0:
        return pal + pal[::-1]
    return pal + s[i] + pal[::-1]

s = 'bbeebeb'
print(palindrome(s))

# time complexity: S^2
# space complexity: S^2
"""
important: parts of a string
- Prefix
- Suffix
- Substring
- Proper ''
"""
