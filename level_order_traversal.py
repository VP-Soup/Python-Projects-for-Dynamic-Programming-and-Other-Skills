def level_order(root):
    if not root:
        return
    q = [root]
    result = []
    while q:
        result.append(q[0].info)
        temp = q.pop(0)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    return result
