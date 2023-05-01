from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
                
        return sorted(count, key=count.get, reverse=True)[:k]