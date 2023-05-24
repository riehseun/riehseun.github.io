class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR is commutative and associative, so can rearrange
        # 1 xor 2 xor 3 xor 1 xor 2 xor 3 xor 4 =
        # (1 xor 1) xor (2 xor 2) xor (3 xor 3) xor 4 =
        # 0 xor 0 xor 0 xor 4 =
        # 4

        xor = 0

        for num in nums:
            xor ^= num

        return xor