class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)

    def binary_search(self, nums, low, high, target):

        if low > high:
            return -1

        mid = low + (high - low) / 2
        mid = int(mid)

        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target and target < nums[mid]:
                return self.binary_search(nums, low, mid-1, target)
            else:
                return self.binary_search(nums, mid+1, high, target)
        else:
            if nums[mid] < target and target <= nums[high]:
                return self.binary_search(nums, mid+1, high, target)
            else:
                return self.binary_search(nums, low, mid-1, target)