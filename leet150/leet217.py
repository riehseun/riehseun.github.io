from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for k,v in count.items():
            if v >= 2:
                return True

        return False
