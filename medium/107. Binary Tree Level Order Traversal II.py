# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        stack = [(root, 0)]
        level_dict = {}

        max_level = 0
        while len(stack) > 0:
            node, level = stack.pop(0)
            
            if level not in level_dict:
                level_dict[level] = []
            level_dict[level].append(node.val)

            if node.left is not None:
                max_level = max(max_level, level + 1)
                stack.append((node.left, level + 1))
            
            if node.right is not None:
                max_level = max(max_level, level + 1)
                stack.append((node.right, level + 1))

        result = []
        i = max_level
        while True:
            if i in level_dict:
                result.append(level_dict[i])
            else:
                break
            i -= 1

        return result   
        