from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for k,v in count.items():
            if v > len(nums)/2:
                return k