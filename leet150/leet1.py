class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_dict = {}
        for i, num in enumerate(nums):
            my_dict[num] = i

        for i, num in enumerate(nums):
            print(target-num)
            if target-num in my_dict and i != my_dict[target-num]:
                return [i, my_dict[target-num]]

        return []