# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree = []
        self.inorder_traverse(root, tree)

        if len(tree)-k >= 0 and k > 0:
            return tree[k-1]

        return None

    def inorder_traverse(self, node, tree):

        if node:
            self.inorder_traverse(node.left, tree)

            if len(tree) == 0:
                tree.append(node.val)
            elif tree[-1] != node.val:
                tree.append(node.val)

            self.inorder_traverse(node.right, tree)