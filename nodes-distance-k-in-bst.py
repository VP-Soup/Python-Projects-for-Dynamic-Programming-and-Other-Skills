"""
find all values in BST that are of K distance to a node with value N given T nodes in the BST
- nodes have unique values and are non-negative
"""


class Node:
    # A constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# time and space O(n)
def distanceK(root, target, k):
    answer = []

    # gets all values k values away from 'root' (e.g. going only 'down')
    def kDown(root, k):
        if root is None or k < 0:
            return
        if k == 0:
            answer.append(root.data)
            return
        kDown(root.left, k - 1)
        kDown(root.right, k - 1)

    # depth first search
    def dfs(root, target, k):
        if root is None:
            return -1
        if root.data == target:
            kDown(root, k)
            return 0

        # dl = distance of left child from target
        dl = dfs(root.left, target, k)

        # checks if target was found in left subtree
        if dl != -1:

            # checks if root is at distance k from target
            if dl + 1 == k:
                answer.append(root.data)
            # if not print all right child units at k - dl - 2 distance - NOTE - 2 since right child is 2 edges away
            else:
                kDown(root.right, k - dl - 2)
            # readjust for parent calls
            return 1 + dl

        # same as above but for right subtree
        dr = dfs(root.right, target, k)
        if dr != -1:
            if dr + 1 == k:
                answer.append(root.data)
            else:
                kDown(root.left, k - dr - 2)
            return 1 + dr
        return -1

    dfs(root, target, k)
    print(answer)
    return answer

# bfs implementation also O(n) time and space
def try2(root, target, k):
    global target_node
    pm = dict()
    stack = [root]
    # worklist algorithm to make dict
    while stack:
        head = stack.pop()
        if head.data == target:
            target_node = head
        if head.left:
            stack.append(head.left)
            if head.left not in pm:
                pm[head.left] = head
        if head.right:
            stack.append(head.right)
            if head.right not in pm:
                pm[head.right] = head
    # data structure for checking if a node already visited in O(log(n))
    visited = set()
    # worklist algorithm for finding k-distance nodes
    stack2 = [(target_node, k), ]
    visited.add(target_node)
    answer = []
    while stack2:
        h, d = stack2.pop()
        if d == 0:
            answer.append(h.data)
            continue
        else:
            if h.left and h.left not in visited:
                visited.add(h.left)
                stack2.append((h.left, d - 1))
            if h.right and h.right not in visited:
                visited.add(h.right)
                stack2.append((h.right, d - 1))
            if h in pm and pm[h] not in visited:
                visited.add(pm[h])
                stack2.append((pm[h], d - 1))
    answer.sort()
    return answer


root = Node(3)
root.left = Node(1)
root.right = Node(5)
root.left.left = Node(0)
root.left.right = Node(2)
root.left.right.right = Node(4)
root.right.right = Node(6)
root.right.right.right = Node(8)
root.right.right.right.left = Node(7)
target = root.right
distanceK(root, 5, 2)
print(try2(root, 5, 2))
