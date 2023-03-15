# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1

        if length == 1:
            return None

        if length == n:
            return head.next

        temp = head
        while length - n - 1 != 0:
            temp = temp.next
            n += 1

        temp.next = temp.next.next
        return head