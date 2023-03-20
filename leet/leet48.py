class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # First reverse up & down
        # Second, swap index i and j

        n = len(matrix)
        start = 0
        end = n - 1
        while start < end:
            matrix[start], matrix[end] = matrix[end], matrix[start]
            start += 1
            end -= 1

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]