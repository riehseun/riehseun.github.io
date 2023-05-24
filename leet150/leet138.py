"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        original_head = head

        # Duplicate each node in the linked list.
        while head:
            temp = head.next
            head.next = Node(head.val)
            if head.next:
                head.next.next = temp

            head = head.next.next

        # Set random pointers for duplicated nodes.
        head = original_head
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next

        # Remove original nodes.
        head = original_head
        original_new_head = None
        while head:
            if head.next:
                temp = head.next
                head.next = head.next.next
                head = temp
                if not original_new_head:
                    original_new_head = head
            else:
                break

        # return original_head
        return original_new_head