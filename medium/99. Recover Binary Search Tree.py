# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nodes = []

        def bfs(root):
            if root.left is not None:
                bfs(root.left)
            nodes.append(root)
            if root.right is not None:
                bfs(root.right)
        bfs(root)

        vals = []

        for node in nodes:
            vals.append(node.val)

        vals_sorted = vals[:]
        vals_sorted.sort()

        print(len(nodes))
        print(vals)
        print(vals_sorted)
        
        node_to_swap = None

        for j in range(len(vals)):
            if vals[j] != vals_sorted[j]:
                if node_to_swap is None:
                    node_to_swap = nodes[j]
                else:
                    temp = node_to_swap.val
                    node_to_swap.val = nodes[j].val
                    nodes[j].val = temp
                    break

        return root