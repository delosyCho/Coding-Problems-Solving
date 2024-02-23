# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if head is None:
            return head

        node = head

        head_check = True
        partition_node = None
        partition_left_node = None
        while node:
            if node.val >= x:
                partition_node = node
                break

            partition_left_node = node            
            node = node.next
            head_check = False
        
        if (partition_node is None or partition_left_node is None) and head_check is False:
            if head.next is not None:
                if head.next.val < x and head.val >= x:
                    head.next.next = head
                    node = head.next
                    head.next = None
                    head = node

            return head
        
        node = partition_node.next
        left_node = partition_node
        
        while node:
            if node.val < x:
                if head_check is False:
                    left_node.next = node.next
                    partition_left_node.next = node
                    node.next = partition_node

                    partition_left_node = node
                else:
                    head_check = False
                    left_node.next = node.next
                    partition_left_node = node
                    partition_left_node.next = partition_node
                    head = partition_left_node
            left_node = node
            node = node.next

        return head
        