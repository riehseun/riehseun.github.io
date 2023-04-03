class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append([])

        num_subset = 2 ** len(nums)

        for i in range(1, num_subset):
            binary = bin(i)
            binary = binary.replace("0b","")
            padding = "0" * (len(nums)-len(binary))
            binary = padding + binary
            subset = []

            for j, bit in enumerate(binary):
                if bit == "1":
                    subset.append(nums[j])
            result.append(subset)

        return result