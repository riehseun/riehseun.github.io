class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n = len(nums1)
        m = len(nums2)

        l = int((m+n+1)/2)
        r = int((m+n+2)/2)
        return (self.find_ith_element(nums1, 0, nums2, 0, l) \
            + self.find_ith_element(nums1, 0, nums2, 0, r)) / 2.0

    def find_ith_element(self, nums1, start1, nums2, start2, i):
        """
        Find ith element of two sorted arrays.

        Args:
            nums1 -- A sorted array.
            start1 -- The starting index to search for the median
                of the combined sorted array in nums1.
            nums2 -- A sorted array.
            start2 -- The starting index to search for the median
                of the combined sorted array in nums2.
            i -- ith element to find.

        Returns:
            The ith element of merged sorted arrays (float)
        """

        # Median cannot exists in numbers smaller than or equal to
        # the smaller median.

        # Example #1:
        # [1,2,3,5,7] and [3,4,6,9,11] and i=5
        # Merged: [1,2,3,3,4,5,6,7,9,11]

        # [1,2,3,5,7] [3,4,6,9,11] i=5
        #  s           s
        # mid1 = nums1[0+2-1=1] = 2
        # mid2 = nums2[0+2-1=1] = 4

        # [1,2,3,5,7] [3,4,6,9,11] i=3
        #      s       s
        # mid1 = nums1[2+1-1=2] = 3
        # mid2 = nums2[0+1-1=0] = 3

        # [1,2,3,5,7] [3,4,6,9,11] i=2
        #      s         s
        # mid1 = nums1[2+1-1=2] = 3
        # mid2 = nums2[1+1-1=1] = 4

        # [1,2,3,5,7] [3,4,6,9,11] i=1
        #        s       s
        # min(5,4) = 4

        n = len(nums1)
        m = len(nums2)

        if start1 > n-1:
            return nums2[start2+i-1]
        if start2 > m-1:
            return nums1[start1+i-1]

        if i == 1:
            return min(nums1[start1], nums2[start2])

        mid1 = 100000000
        mid2 = 100000000
        if start1+i/2-1 < n:
            mid1 =  nums1[start1+int(i/2)-1]
        if start2+i/2-1 < m:
            mid2 =  nums2[start2+int(i/2)-1]

        if mid1 < mid2:
            # We are rejecting elements that are less than smaller
            # median. We are adjusting ith element to find accordingly.
            return self.find_ith_element(
                nums1, start1+int(i/2), nums2, start2, i-int(i/2))
        else:
            return self.find_ith_element(
                nums1, start1, nums2, start2+int(i/2), i-int(i/2))