class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        nums_copy = self.nums[:]
        for i in range(len(nums_copy)-1, 0, -1):
            j = random.randrange(0, i+1)
            nums_copy[i], nums_copy[j] = nums_copy[j], nums_copy[i]
        return nums_copy


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()