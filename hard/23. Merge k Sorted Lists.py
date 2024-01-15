# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        div = 2
        while True:
            for i in range(len(lists) // 2):
                head = None
                new_node = None

                if i * div + div // 2 >= len(lists):
                    continue

                right = lists[i * div]
                left = lists[i * div + div // 2]
                print('node:', i * div, i * div + div // 2)
                while right is not None or left is not None:
                    if right is not None or left is not None:
                        if right is None:
                            if head is None:
                                head = left
                                new_node = head
                            else:
                                head.next = left
                                head = head.next
                            print(i * div, 'left', left.val)
                            left = left.next
                        elif left is None:
                            if head is None:
                                head = right
                                new_node = head
                            else:
                                head.next = right
                                head = head.next
                            print(i * div, 'right', right.val)
                            right = right.next
                        
                        elif right.val < left.val:
                            if head is None:
                                head = right
                                new_node = head
                            else:
                                head.next = right
                                head = head.next
                            print(i * div, 'right', right.val, left.val)
                            right = right.next
                        else:
                            if head is None:
                                head = left
                                new_node = head
                            else:
                                head.next = left
                                head = head.next
                            print(i * div, 'left', right.val, left.val)
                            left = left.next
                        
                lists[i * div] = new_node
                head = new_node
                arr = []
                while head is not None:
                    arr.append(head.val)
                    head = head.next
                print('arr', arr)
            div = div * 2
            if div // 2 >= len(lists):
                break

        return lists[0]