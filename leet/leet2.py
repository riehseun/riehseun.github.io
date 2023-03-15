# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        carry = 0

        while l1 and l2:
            val = (l1.val + l2.val + carry) % 10
            print(val)
            if l1.val + l2.val + carry >= 10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next

            if not prev:
                prev = ListNode(val, None)
                head = prev
            else:
                prev.next = ListNode(val, None)
                prev = prev.next

        while l1:
            val = (l1.val + carry) % 10
            print(val)
            if l1.val + carry >= 10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            prev.next = ListNode(val, None)
            prev = prev.next

        while l2:
            val = (l2.val + carry) % 10
            print(val)
            if l2.val + carry >= 10:
                carry = 1
            else:
                carry = 0
            l2 = l2.next
            prev.next = ListNode(val, None)
            prev = prev.next

        if carry == 1:
            prev.next = ListNode(1, None)
            prev = prev.next

        return head