from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 1:
            return len(points)

        result = 1

        # Compute the slope between all pairs of points.
        # Most frequent slope will form the line.
        for i in range(len(points)):
            # Create a new dictionary for each point!
            frequency = defaultdict(int)
            for j in range(i+1, len(points)):
                if points[i][0] != points[j][0]:
                    slope = (points[i][1]-points[j][1]) / (points[i][0]-points[j][0])
                    frequency[slope] += 1
                    result = max(frequency[slope], result)
                # In case of infinite slope (Or vertical line)
                else:
                    frequency[math.inf] += 1
                    result = max(frequency[math.inf], result)

        return result+1