# height of a binary tree with root at height 0
def height(root):
    if root:
        if root.left or root.right:
            return 1 + max(height(root.left), height(root.right))
        else:
            return 0
    else:
        return 0

# Time complexity: O(n)
# Space complexity: O(n)
