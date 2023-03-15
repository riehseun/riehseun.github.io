class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.binary_search(nums, 0, len(nums)-1, target)

    def binary_search(self, nums, low, high, target):

        if low > high:
            return [-1, -1]

        mid = low + (high - low) / 2
        mid = int(mid)

        if target > nums[mid]:
            return self.binary_search(nums, mid+1, high, target)
        elif target < nums[mid]:
            return self.binary_search(nums, low, mid-1, target)
        else:
            # return mid
            start = mid
            while nums[mid] == nums[start]:
                start -= 1
                if start < 0:
                    break
            start += 1

            end = mid
            while nums[mid] == nums[end]:
                end += 1
                if end >= len(nums):
                    break
            end -= 1

            return [start, end]