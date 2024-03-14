# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        tail = None

        N = 1

        tail = head
        while tail.next:
            tail = tail.next
            N += 1
        

        i = 1
        middle_point = N // 2 + N % 2

        node = head
        last_node = None

        while node.next:
            temp = node
            node = node.next
            if i == middle_point:
                temp.next = None
            elif i > middle_point:
                temp.next = last_node
                
            last_node = temp
            i += 1
        tail.next = last_node

        i = 1
        node = head
        while i <= N // 2:
            temp = node
            node = node.next

            temp2 = tail
            tail = tail.next
            
            temp.next = temp2
            temp2.next = node
            
            i += 1


