# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        # Time: O(n) where n is the number of nodes.
        # Space: O(1)
        return self.helper(root, 0)


    def helper(self, node, depth):

        if not node:
            return depth

        # Each time the recursive call is made, increase the depth by 1.
        return max(self.helper(node.left, depth+1), \
            self.helper(node.right, depth+1))