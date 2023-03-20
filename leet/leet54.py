class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Remove rows and columns from the matrix while moving spiral.
        # The order is
        #   Remove first row
        #   Remove last col
        #   Remove last row
        #   Remove first col
        # Repeat

        result = []

        while matrix:
            nums = matrix.pop(0)  # Remove first row.
            result += nums

            if matrix and matrix[0]:
                for row in matrix:
                    num = row.pop()  # Remove last col.
                    result += [num]

            if matrix:
                nums = matrix.pop()  # Remove last row.
                # Ensure the order that numbers are appended to the result.
                nums.reverse()
                result += nums

            if matrix and matrix[0]:
                # Ensure the order that numbers are appended to the result.
                matrix_copy = matrix.copy()
                matrix_copy.reverse()
                for row in matrix_copy:
                    num = row.pop(0)  # Remove first col.
                    result += [num]

        return result