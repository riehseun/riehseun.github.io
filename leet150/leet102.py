from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result = defaultdict(list)
        self.bfs(root, result)

        final_result = []
        for k,v in result.items():
            final_result.append(v)

        return final_result

    def bfs(self, root, result):
        level = 0

        queue = deque()
        queue.append((root, root.val, level))

        explored = set()
        explored.add(root)

        while queue:
            node, node.val, level = queue.popleft()
            result[level].append(node.val)
            if node.left:
                if node.left.val not in explored:
                    explored.add(node.left)
                    queue.append((node.left, node.left.val, level+1))
            if node.right:
                if root.right.val not in explored:
                    explored.add(node.right)
                    queue.append((node.right, node.right.val, level+1))

        return result