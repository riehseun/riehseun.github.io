class Solution:
    def canJump(self, nums: List[int]) -> bool:

        target_index = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= target_index:
                target_index = i

        if target_index == 0:
            return True

        return False