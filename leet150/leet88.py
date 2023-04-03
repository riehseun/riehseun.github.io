from heapq import heappush, heappop

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        min_heap = []
        for i in range(m):
            heappush(min_heap, nums1[i])

        for j in range(n):
            heappush(min_heap, nums2[j])

        k = 0
        while min_heap:
            nums1[k] = heappop(min_heap)
            k += 1

        return nums1