# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        left_node, right_node = head, head

        if left == right:
            return head

        for _ in range(left - 2):
            left_node = left_node.next
        left_node_parent = left_node
        if left > 1:
            left_node = left_node.next

        for _ in range(right - 1):
            right_node = right_node.next
        leaf_node = right_node.next

        if right - left == 1:
            print('check', left_node.val, right_node.val)
            
            if left > 1:
                left_node_parent.next = right_node
            else:
                head = right_node
            right_node.next = left_node
            left_node.next = leaf_node
            return head

        next_node = left_node

        n = right - left + 1
        for i in range(n):
            if i == n - 1:
                if left > 1:
                    left_node_parent.next = next_node
                else:
                    head = right_node
            if next_node is None:
                break

            temp_node = next_node.next

            next_node.next = leaf_node
            leaf_node = next_node

            next_node = temp_node
        
        return head
