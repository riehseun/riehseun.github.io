from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []
        queue = deque()

        # Compute the maximum in the first window.
        for i in range(k):

            # Pop out all smaller items than the current item
            # by removing last items in the queue.
            # Then the first itme in the queue will always
            # contains the maximum item.
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

        result.append(nums[queue[0]])

        # Move the window
        for i in range(k, len(nums)):

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

            # Remove all indexes in the queue that is before
            # and outside than the current window.
            while queue and queue[0] <= (i - k):
                queue.popleft()

            result.append(nums[queue[0]])

        return result