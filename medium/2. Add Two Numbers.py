# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        add_value = 0

        result = None
        cur_node = None

        while True:
            value = add_value
            if node1 is not None:
                value += node1.val
                
            if node2 is not None:
                value += node2.val
                
            if add_value == 0 and node1 is None and node2 is None:
                break
            
            if value >= 10:
                value -= 10
                add_value = 1
            else:
                add_value = 0
            
            # print(value, add_value)
            node = ListNode(val=value)
            if result is None:
                result = node
                cur_node = node
            else:
                cur_node.next = node
                cur_node = node

            if node1 is not None:
                value += node1.val
                node1 = node1.next

            if node2 is not None:
                value += node2.val
                node2 = node2.next
            
        return result

