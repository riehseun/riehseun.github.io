class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        min_num = -(2**31)
        max_num = 2**31 - 1

        if (dividend >= 0 and divisor < 0) \
            or (dividend < 0 and divisor >= 0):
            sign = -1
        else:
            sign = 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        # Key idea.
        result = len(range(0, dividend-divisor+1, divisor))

        if sign == -1:
            result = -result

        result = min(max_num, result)
        result = max(min_num, result)

        return result