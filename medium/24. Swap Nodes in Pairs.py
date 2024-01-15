# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        if head.next is None:
            return head

        node_to_swap = head.next
        temp = node_to_swap.next

        node_to_swap.next = head
        head.next = temp

        head = node_to_swap

        node_for_swap = head.next

        while True:
            if node_for_swap.next is None:
                break
            if node_for_swap.next.next is None:
                break

            node_to_swap_1 = node_for_swap.next
            node_to_swap_2 = node_for_swap.next.next
            # print(node_to_swap_1.val, node_to_swap_2.val)
            
            # temp = node_to_swap_2.next
            node_for_swap.next = node_to_swap_2
            node_to_swap_1.next = node_to_swap_2.next
            node_to_swap_2.next = node_to_swap_1

            node_for_swap = node_to_swap_1
            print(node_for_swap.val)
        return head
            
            




        return head



