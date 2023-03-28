class Solution(object):
    def climbStairs(self, n):
        
        # Dictionary to store the answer for each n.
        memory = {}
        memory[1] = 1
        memory[2] = 2

        # Example: n=1
        # 1+1
        # 1

        # Example: n=2
        # 1+1, 2
        # 2

        # Example: n=3
        # 1+2, 2+1, 1+1+1
        # 3

        # Example: n=4
        # 1+1+2, 1+2+1, 2+1+1, 2+2, 1+1+1+1
        # 5

        # Example: n=5
        # 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1,
        # 1+1+1+1+1
        # 8

        # Take 1 step and compute (n-1)
        # Take 2 steps and compute (n-2)

        return self.subroutine(n, memory)


    def subroutine(self, n, memory):

        if n in memory:
            return memory[n]

        memory[n] = self.subroutine(n-1, memory) + self.subroutine(n-2, memory)
        return memory[n]