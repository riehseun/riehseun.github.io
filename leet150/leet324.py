class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Sort the array
        # Put smaller half in even indexes
        # Put larger half in odd indexes

        nums_copy = nums.copy()
        nums_copy.sort()
        print(nums_copy)
        print(nums)

        mid = len(nums)//2-1

        j = 0
        for i in range(0, len(nums), 2):
            nums[i] = nums_copy[j]
            j += 1

        for i in range(1, len(nums), 2):
            nums[i] = nums_copy[j]
            j += 1
            
        return nums