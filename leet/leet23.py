# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode()
        temp = head

        # This list will store all node in all linked lists. 
        all_nodes = []  

        for node in lists:
            while node:
                all_nodes.append(node)
                node = node.next

        # Sort node by value. 
        all_nodes.sort(key=lambda x:x.val)

        for node in all_nodes:
            head.next=node
            head=head.next
        
        return temp.next