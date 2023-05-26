class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        largest = -math.inf
        prod = 1
        is_default_prod = True

        for num in nums:
            if num == 0:
                prod = 1
            else:
                prod *= num
                if prod == 1:
                    is_default_prod = False
            largest = max(largest, prod)

        prod = 1
        nums.reverse()
        for num in nums:
            if num == 0:
                prod = 1
            else:
                prod *= num
                if prod == 1:
                    is_default_prod = False
            largest = max(largest, prod)

        if largest == 1 and is_default_prod:
            return 0

        return largest