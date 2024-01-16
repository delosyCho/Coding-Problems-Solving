# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        num_of_node = 0
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next

        if len(nodes) == 0:
            return None
        
        if len(nodes) == 1:
            return head

        if len(nodes) == 2:
            if k % 2 == 1:
                last_node = head.next
                head.next = None
                last_node.next = head
                return last_node

        k = k % len(nodes)
        print('k', k)

        for _  in range(k):
            first_node = nodes[0]
            last_node =  nodes.pop()
            print(first_node.val, last_node.val)
            nodes[-1].next = None
            last_node.next = first_node

            nodes.insert(0, last_node)

        return nodes[0]

        
        