# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root))

    def helper(self, root):
        if root == None:
            return [0, 0]

        left_subtree = self.helper(root.left)
        right_subtree  = self.helper(root.right)
        include_root = root.val + left_subtree[1] + right_subtree[1]
        exclude_root = max(left_subtree) + max(right_subtree)

        return [include_root, exclude_root]