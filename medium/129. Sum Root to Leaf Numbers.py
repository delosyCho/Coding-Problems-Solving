# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total_sum = 0

        stack = [[root, 0]]

        while stack:
            node, value = stack.pop()

            node_value = value * 10 + node.val

            if node.right is not None:
                stack.append([node.right, node_value])
            if node.left is not None:
                stack.append([node.left, node_value])
            if node.right is None and node.left is None:
                total_sum += node_value

        return total_sum
        