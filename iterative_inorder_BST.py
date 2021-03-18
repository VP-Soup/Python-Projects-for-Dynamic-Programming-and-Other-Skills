from collections import *
def inOrderBSTreeTraversal(root):
    stack = []
    current = root
    result = []
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.data)
            current = current.right
    return result