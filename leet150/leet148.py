# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Convert linked list into a list and sort it.
        elements = []

        original_head = head
        while head:
            elements.append(head.val)
            head = head.next

        elements.sort()

        # Created new ;inked list based on sorted list.
        head = original_head
        prev = None
        orignal_head = None
        for num in elements:
            node = ListNode(num)
            if not prev:
                prev = node
                original_head = prev
            else:
                prev.next = node
                prev = node

        return original_head