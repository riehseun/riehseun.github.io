# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # Traverse A then B. Or traverse B then A.
        # Either way, there will be a loop at the start of the intersection.

        head = headA

        # Connect linked lists A and B.
        while head.next:
            head = head.next
        head.next = headB

        fast = slow = headA
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = headA
                while fast != slow:
                    slow, fast = slow.next, fast.next
                head.next = None
                return slow

        # No loop found
        head.next = None
        return None






