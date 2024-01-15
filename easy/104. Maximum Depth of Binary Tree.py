# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(root, depth):
    if root is None:
        return depth
    
    depth_l = dfs(root.left, depth + 1)
    depth_r = dfs(root.right, depth + 1)
    
    return max([depth_l, depth_r])

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return dfs(root, 0)        
        