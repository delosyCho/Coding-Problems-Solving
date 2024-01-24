# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = None
        result_head = None

        while head:
            register = False
            
            if head.next is not None:
                if head.next.val == head.val:
                    check_val = head.val

                    while True:
                        if head.next and head.next.val == check_val:
                            head = head.next
                        else:
                            break
                else:
                    register = True
            else:
                register = True
            
            if head is None:
                print('check')
                break

            print(register, head.val)
            if register is True:
                if result is None:
                    result = head
                    result_head = head
                else:
                    result.next = head
                    result = result.next
                    
            head = head.next

        if result is not None:
            result.next = None

        return result_head