class Solution:
    def numSquares(self, n: int) -> int:

        # count_num_squares[i] = min number of perfect squares that sum to i)

        count_num_squares = []
        count_num_squares.append(0)
        for _ in range(1, n+1):
            count_num_squares.append(10000)

        for i in range(1, n+1):
            j = 1
            while j*j <= i:

                count_num_squares[i] = min(count_num_squares[i], count_num_squares[i-j*j]+1)
                j += 1

        return count_num_squares[n]