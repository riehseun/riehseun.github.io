from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = []

        for i in range(k):
            heappush(min_heap, nums[i])

        for j in range(k, len(nums)):
            if nums[j] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[j])

        return heappop(min_heap)