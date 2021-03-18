"""
There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by .
If you join  adjacent buildings, they will form a solid rectangle of area .

For example, the heights array . A rectangle of height  and length  can be constructed within the boundaries.
The area formed is .
"""

# https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
from collections import *

def largestRectangle(h):
    stack = []
    max_a = 0
    i = 0
    while i < len(h):
        if (not stack) or (h[stack[-1]] <= h[i]):
            stack.append(i)
            i += 1
        else:
            height = stack.pop()
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            area = h[height] * width
            max_a = max(area, max_a)
    while stack:
        height = stack.pop()
        if stack:
            width = i - stack[-1] - 1
        else:
            width = i
        area = h[height] * width
        max_a = max(area, max_a)
    return max_a

def largestRectangle2(h):
    s = Stack()
    Area = 0
    for right in range(len(h)+1):
        left = 0
        current_height = h[right]
        if s and current_height < s.top().height:
            left, height = s.pop()
            width = right - left
            Area = max(Area, width*height)
        else:
            s.push((left, current_height))
