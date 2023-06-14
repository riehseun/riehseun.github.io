# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Jump 2 steps.

        if not head:
            return None

        temp = head
        prev = None
        original_prev = None

        while head:
            node = ListNode(head.val)
            if not prev:
                prev = node
                original_prev = prev
            else:
                prev.next = node
            prev = node

            if head.next:
                head = head.next.next
            else:
                break

        head = temp
        head = head.next

        while head:
            node = ListNode(head.val)
            prev.next = node
            prev = node

            if head.next:
                head = head.next.next
            else:
                break

        return original_prev