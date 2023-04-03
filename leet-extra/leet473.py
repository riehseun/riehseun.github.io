class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        side_length = total_length // 4
        if max(matchsticks) > side_length:
            return False

        matchsticks.sort()
        matchsticks.reverse()

        return self.helper(0, matchsticks, [0,0,0,0], side_length)


    def helper(self, i, matchsticks, sides, side_length):
        # Used all the sticks.
        if i == len(matchsticks):

            formed_square = True
            for side in sides:
                if side != side_length:
                    formed_square = False

            if formed_square:
                return True
            else:
                return False

        for j in range(4):
            if matchsticks[i] <= side_length - sides[j]:
                # Use the stick.
                new_sides = sides.copy()
                new_sides[j] += matchsticks[i]
                if self.helper(i+1, matchsticks, new_sides, side_length):
                    return True

        # If cannot use all the sticks.
        return False