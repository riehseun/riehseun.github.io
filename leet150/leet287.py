class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Convert nums[num] to its negative
        for num in nums:
            num = abs(num)
            if nums[num] < 0:
                return num
            nums[num] = -nums[num]

        return len(nums)