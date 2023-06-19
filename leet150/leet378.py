from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        # 1  5  9
        # 10 11 13
        # 12 13 15

        # Kth smallest among N sorted rows

        n = len(matrix)
        m = len(matrix[0])
        min_heap = []

        for i in range(min(n,k)):
            heappush(min_heap, (matrix[i][0], i, 0))

        val = min_heap[0][0]
        for _ in range(k):
            val, i, j = heappop(min_heap)
            if j < m-1:
                heappush(min_heap, (matrix[i][j+1], i, j+1))

        return val