# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.run(head, head)

    def run(self, slow, fast):

        if slow:
            slow = slow.next

        if not fast or not fast.next:
            return False

        fast = fast.next.next

        if slow == fast:
            return True

        return self.run(slow, fast)