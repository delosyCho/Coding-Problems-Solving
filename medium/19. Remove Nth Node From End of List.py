# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        num_of_nodes = 0
        node = head
        while True:
            if node is not None:
                num_of_nodes += 1
            else:
                break
            node = node.next

        if num_of_nodes == 1:
            return None

        if num_of_nodes == n:
            head = head.next
            return head

        node = head
        for _ in range(num_of_nodes - 1 - n):
            node = node.next
        node.next = node.next.next

        return head