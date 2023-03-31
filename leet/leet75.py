class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low = 0
        high = len(nums) - 1
        mid = 0

        while mid <= high:
            # Incorrect place. Move the 0 to the beginning.
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            # Correct place.
            elif nums[mid] == 1:
                mid += 1
            # Incorrect place. Move the 2 to the end.
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

        return nums