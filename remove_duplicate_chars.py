"""
Name: Vicente James Perez
Date: 1/09/2020
Assignment: COT4401 - Remove duplicates of 3x letter
Due Date: 1/10/2020
About this project:
Assumptions:NA
All work below was performed by Vicente James Perez
"""

def remove_duplicates2(s):
    tokens = list(s)
    duplicate_counter = 0
    for i in range(len(tokens)):
        if i>0 and tokens[i] == tokens[i - 1]:
                duplicate_counter += 1
        elif duplicate_counter >= 3:
            for n in range(1, duplicate_counter+1):
                tokens[i-n]=''
            break
        else:
            duplicate_counter = 1
    new_string =  "".join(tokens)
    if new_string == s:
        return new_string
    else:
        return remove_duplicates(new_string)


def remove_duplicates(s):
    stk = list()
    for c in s:
        if not stk:
            stk.insert(0, [c, 1])
        elif stk[0][0] == c:
            stk[0][1] += 1
        else:
            stk.insert(0, [c, 1])
    solution = list()
    while stk:
        c, freq = stk.pop()
        if solution and solution [-1][0] == c and solution [-1][1] + freq >= 3:
            solution.pop()
            continue
        elif freq >= 3:
            continue
        else:
            solution.append([c, freq])
    result = ''
    for c, freq in solution:
        result += c*freq
    return result


string = 'BAAABBBBCCA'
result = remove_duplicates(string)
print(result)