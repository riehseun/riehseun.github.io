class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permute_helper(result, nums, 0, len(nums)-1)
        return result

    def permute_helper(self, result, nums, start, end):
        if start == end:
            result.append(nums)
            return
        else:
            for i in range(start, end+1):
                nums_copy = nums.copy()
                nums_copy[i], nums_copy[start] = nums_copy[start], nums_copy[i]
                self.permute_helper(result, nums_copy, start+1, end)