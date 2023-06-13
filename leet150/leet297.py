# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def pre_order_traversal(node):
            if node is not None:
                tree.append(str(node.val))
                pre_order_traversal(node.left)
                pre_order_traversal(node.right)
            else:
                tree.append("X")

        tree = []
        pre_order_traversal(root)
        return " ".join(tree)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def decode():
            val = next(values)
            if val != "X":
                node = TreeNode(int(val))
                node.left = decode()
                node.right = decode()
                return node
            else:
                return None

        values = iter(data.split(" "))
        return decode()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))