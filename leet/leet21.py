# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        temp = result

        # Time: O(n) where n is the combined lenght of two linked lists.
        # Space: O(1) no additional space allocated.
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next

        if list1:
            result.next = list1
        if list2:
            result.next = list2

        # Returning result.next will return the last node in the linked
        # list we computed. To return the first node, we use temp.
        return temp.next