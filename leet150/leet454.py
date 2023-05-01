from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Compute all possible sum between nums1 & nums2, nums3 & nums4
        # Check sum between two groups to see if it becomes 0

        sum1 = defaultdict(int)

        for i in nums1:
            for j in nums2:
                sum1[i+j] += 1

        sum2 = defaultdict(int)

        for k in nums3:
            for l in nums4:
                sum2[k+l] += 1

        count = 0
        for k1 in sum1.keys():
            for k2 in sum2.keys():
                if k1 + k2 == 0:
                    count += (sum1[k1]*sum2[k2])

        return count