class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        n, remainder = divmod(abs(numerator), abs(denominator))

        if numerator * denominator < 0:
            sign = "-"
        else:
            sign = ""

        result = [sign+str(n), "."]
        stack = []

        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))

        index = stack.index(remainder)
        result.insert(index+2, "(")
        result.append(")")

        return "".join(result).replace("(0)", "").rstrip(".")