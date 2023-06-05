# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        pre = None
        cur = head
        nex = head.next

        while cur:
            cur.next = pre
            pre = cur
            cur = nex
            if nex:
                nex = nex.next

        return pre