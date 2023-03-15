class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []

        self.subroutine(n, 0, 0, "", combinations)

        return combinations

    def subroutine(self, n, num_open, num_close, string, combinations):
        if num_open == n and num_close == n:
            combinations.append(string)

        if num_open < n:
            # No "return" statement.
            self.subroutine(n, num_open+1, num_close, string+"(", combinations)

        # Number of closing parenthesie cannot exceed the number of
        # opening parenthesis at any point to construct valid patterns.
        if num_close < num_open:
            # No "return" statement.
            self.subroutine(n, num_open, num_close+1, string+")", combinations)