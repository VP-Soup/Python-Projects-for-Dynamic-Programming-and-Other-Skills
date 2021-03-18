# Checks if a given binary tree is a BST

def check_binary_search_tree_(root):

    def sub_check(sub_root, left_limit=float('-inf'), right_limit=float('inf')):
        if not sub_root:
            return True
        if left_limit >= sub_root.data or right_limit <= sub_root.data:
            return False
        return sub_check(sub_root.left, left_limit, sub_root.data) and sub_check(sub_root.right, sub_root.data, right_limit)
