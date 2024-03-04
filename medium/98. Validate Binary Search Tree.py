# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes_to_visit = []
        # nodes_to_visit.append((root, 0))
        # while nodes_to_visit:
        #     node, count = nodes_to_visit.pop(0)
        #     print(node.val, count)
        #     if node.left is not None:
        #         nodes_to_visit.append((node.left, count + 1))
        #     if node.right is not None:
        #         nodes_to_visit.append((node.right, count + 1))
            

        nodes_to_visit.append(
            (root, None, None)
        )

        while nodes_to_visit:
            node, lower_bound, higher_bound = nodes_to_visit.pop()

            if lower_bound is not None:
                if node.val >= lower_bound.val:
                    print(node.val)
                    return False
            
            if higher_bound is not None:
                if node.val <= higher_bound.val:
                    print(node.val, lower_bound, higher_bound)
                    return False

            if node.left is not None:
                nodes_to_visit.append((node.left, node, higher_bound))
                    
            if node.right is not None:
                nodes_to_visit.append((node.right, lower_bound, node))
        return True