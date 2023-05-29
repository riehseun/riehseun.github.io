class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # Binary search trying to find local max.
        return self.helper(0, len(nums)-1, nums)

    def helper(self, low, high, nums):

        mid1 = int((low+high)/2)
        mid2 = mid1 + 1

        if low == high:
            return low

        if nums[mid1] > nums[mid2]:
            return self.helper(low, mid1, nums)
        else:
            return self.helper(mid2, high, nums)