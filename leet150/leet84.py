class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # Store the index of first smaller element to the left of each element.
        left = [-1] * len(heights)

        for i in range(1, len(heights)):
            p = i - 1

            while p >= 0 and heights[p] >= heights[i]:
                p = left[p]

            left[i] = p

        # Store the index of first smaller element to the right of each element.
        right = [len(heights)] * len(heights)

        for i in range(len(heights)-2, -1, -1):
            p = i + 1

            while p < len(heights) and heights[p] >= heights[i]:
                p = right[p]

            right[i] = p

        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, (right[i]-left[i]-1)*heights[i])

        return max_area