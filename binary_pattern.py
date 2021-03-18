# Given binary bit string which mixed with '?'s, list all the differnt binary stringsn by replacing '?' with 0 and 1.

list = []
def binary_pattern(s):
    if '?' in s:
        s_0 = s.replace('?', '0', 1)
        s_1 = s.replace('?', '1', 1)
        binary_pattern(s_0)
        binary_pattern(s_1)
    else:
        list.append(s)
    list.sort()
    return list
