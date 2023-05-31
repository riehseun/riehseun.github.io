class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums_save = nums[:]
        
        for i, num in enumerate(nums):
            new_index = (i+k) % len(nums)
            nums[new_index] = nums_save[i]

        return nums