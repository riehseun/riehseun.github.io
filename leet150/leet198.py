class Solution:
    def rob(self, nums: List[int]) -> int:

        # a) rob the current house
        # b) don't rob the current house
        # max(current + rob(i-2), rob(i-1))

        prev1 = 0
        prev2 = 0

        for num in nums:
            temp = prev1
            prev1 = max(num+prev2, prev1)
            prev2 = temp

        return prev1