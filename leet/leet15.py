class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        if len(nums) < 3:
            return triplets

        nums.sort()  # O(nlogn)

        for i, num in enumerate(nums):
            # If three sum with the same previous number is checked, skip.
            if i > 0 and num == nums[i - 1]:
                continue

            start = i + 1
            end = len(nums) - 1

            while start < end:
                # If the sum is less than zero, need to increment the
                # start index to increase the sum.
                if nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                # If the sum is greater than zero, need to decrement the
                # end index to decrease the sum.
                elif nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                else:
                    triplets.append([nums[i],nums[start],nums[end]])

                    # We can increment either start or end.
                    if nums[start] <= nums[end]:
                        start += 1
                    else:
                        end -= 1

        unique_triplets = []
        for triplet in triplets:
            if triplet not in unique_triplets:
                unique_triplets.append(triplet)

        return unique_triplets