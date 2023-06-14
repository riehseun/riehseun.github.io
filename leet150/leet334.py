from heapq import heappush

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # Always remember the first and second miminum seen so far

        first = math.inf
        second = math.inf

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            # num is greater than both first and second.
            else:
                return True

        return False