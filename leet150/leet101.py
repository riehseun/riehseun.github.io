# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True

        if (not left and right) \
            or (left and not right):
            return False

        if left.val != right.val:
            return False
        else:
            out_pair = self.helper(left.left, right.right)
            in_pair = self.helper(left.right, right.left)

            # If one of them is False, should return False.
            return out_pair and in_pair