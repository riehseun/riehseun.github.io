from heapq import heappush, heappop

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        events = []

        # Start building events.
        for x1, x2, h in buildings:
            events.append((x1,x2,h))

        # End building events. (Building with 0 heights)
        for x1, x2, h in buildings:
            events.append((x2,0,0))

        events.sort(key = lambda x: (x[0], -x[2]))

        result = [[0,0]]  # [x1, h]
        live = [[0, math.inf]]  # [h, x2]

        for x1, x2, h in events:
            # Remove all buildings that have ended within intervals.
            while live[0][1] <= x1:
                heappop(live)

            # If start event, set the building alive.
            if h:
                heappush(live, [-h, x2])

            if result[-1][1] != -live[0][0]:
                result += [ [x1, -live[0][0]] ]

        return result[1:]
