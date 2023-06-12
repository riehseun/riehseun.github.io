class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Consider numbers at the first row
        # If it is greater than target, the entire column is out of scope.
        # Consider numbers at the first column.
        # If it is greater than target, the entire row is out of scope.
        
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                continue  # Move to the next row.
            for j in range(len(matrix[0])):
                if matrix[0][j] > target:
                    break  # Move to the next column.
                if matrix[i][j] == target:
                    return True

        return False