# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        stack = [[root, []]]

        result = []

        while stack:
            node, path = stack.pop()
            path.append(node.val)

            if node.right is None and node.left is None:
                sum_value = sum(path)
                if sum_value == targetSum:
                    result.append(path[:])
            if node.right is not None:
                stack.append([node.right, path[:]])
            if node.left is not None:
                stack.append([node.left, path[:]])


        return result
