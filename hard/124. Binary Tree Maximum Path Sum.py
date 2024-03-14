# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def search_tree(node, arr):
    r_value = 0
    l_value = 0
    
    # is_root = False
    # if len(arr) == 0:
    #     is_root = True

    if node.right is not None:
        r_value = search_tree(node.right, arr)
    if node.left is not None:
        l_value = search_tree(node.left, arr)
    
    max_value = max(r_value + node.val, l_value + node.val, node.val)
    if node.right is None and node.left is None:
        max_value = node.val
    
    arr.append(max(r_value + node.val, l_value + node.val, r_value + l_value + node.val, node.val))
    return max_value


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr = []
        search_tree(root, arr)

        return max(arr)

        








