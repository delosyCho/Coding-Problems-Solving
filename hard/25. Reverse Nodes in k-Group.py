# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node_lists = []
        
        node = head
        while node:
            node_lists.append(node)
            node = node.next
        
        for n in range(len(node_lists) // k):
            add = n * k

            for i in list(reversed(range(1, k))):
                ix = i + add
                print(ix, ix - 1)
                node_lists[ix].next = node_lists[ix - 1]
            
            if (n + 1) * k < len(node_lists):
                node_lists[add].next = node_lists[(n + 1) * k]
                print('check', add, (n + 1) * (len(node_lists) // k))
            else:
                node_lists[add].next = None

            if n > 0:
                node_lists[(n - 1) * k].next = node_lists[add + k - 1]

            if n == 0:
                # print('add', add)
                head = node_lists[add + k - 1]

        node = head
        for _ in range(20):
            if node is not None:
                print(node.val)
                node = node.next

        return head


        
        