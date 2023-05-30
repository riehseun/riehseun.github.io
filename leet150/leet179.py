class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        self.quicksort(nums, 0, len(nums)-1)
        str_nums = []
        for num in nums:
            str_nums.append(str(num))
        return str(int("".join(str_nums)))

    def quicksort(self, nums, l, r):
        if l >= r:
            return
        pos = self.partition(nums, l, r)
        self.quicksort(nums, l, pos-1)
        self.quicksort(nums, pos+1, r)

    def partition(self, nums, l, r):
        low = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

    def compare(self, x, y):
        return str(x) + str(y) > str(y) + str(x)