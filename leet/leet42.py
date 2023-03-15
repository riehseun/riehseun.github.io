class Solution:
    def trap(self, height: List[int]) -> int:
        # Water that each block i can contain is
        # min(max_height_left_side, max_height_right_side) - height[i]

        max_left = 0
        max_right = 0
        left = 0
        right = len(height)-1
        area = 0

        while left <= right:
            if height[left] < height[right]:
                max_left = max(max_left, height[left])
                area += (max_left-height[left])
                left += 1
            else:
                max_right = max(max_right, height[right])
                area += (max_right-height[right])
                right -= 1

        return area