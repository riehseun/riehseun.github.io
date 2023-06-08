# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # It is not possible to really delte this node.
        # But, can copy data of next node to current node, then delete
        # the next node

        node.val = node.next.val
        temp = node.next
        node.next = node.next.next
        temp.next = None