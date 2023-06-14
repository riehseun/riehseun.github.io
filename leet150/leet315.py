class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        result = [0] * len(nums)
        self.helper(0, len(nums), nums, result)
        return result

    def helper(self, low, high, nums, result):

        if low >= high:
            return

        mid = low + ((high-low)//2)
        # mid = (high+low) // 2
        mid = int((high+low)/2)

        self.helper(low, mid, nums, result)
        self.helper(mid+1, high, nums, result)

        left = low
        right = mid + 1
        merged = []
        count = 0

        # Compute the count of smaller items to the right
        # for each number.
        while left < mid+1 and right <= high:
            if nums[left] > nums[right]:
                count + 1
                merged.append(nums[right])
                right += 1
            else:
                result[nums.index(nums[left])] += count
                merged.append(nums[left])
                left += 1

        # Do merge sort
        while left < mid+1:
            result[nums.index(nums[left])] += count
            merged.append(nums[left])
            left += 1

        while right <= high:
            merged.append(nums[right])
            right += 1

        pos = low
        for num in merged:
            nums[pos] = num
            pos += 1







