# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if inorder:

            root_val = preorder.pop(0)  # This is root node.
            root_index = inorder.index(root_val)

            node = TreeNode(root_val)
            node.left = self.buildTree(preorder, inorder[:root_index])
            node.right = self.buildTree(preorder, inorder[root_index+1:])

            return node