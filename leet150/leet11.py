class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        start = 0
        end = len(height) - 1

        while start < end:
            width = end - start
            length = min(height[start], height[end])
            area = width * length
            max_area = max(max_area, area)
            # print("w:"+str(width) + " l:"+str(length) + " a:"+str(area))

            # Max area can only be constructed by keeping higher height.
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return max_area