class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing whitespaces.
        if not s:
            return 0

        neg = False
        if s[0] == "-":
            neg = True
            s  = s[1:]
        elif s[0] == "+":
            s  = s[1:]

        breaking_index = -1
        for i, c in enumerate(s):
            if not c.isdigit():
                breaking_index = i
                break

        if breaking_index != -1:
            if breaking_index == 0:
                return 0
            else:
                s = s[:breaking_index]

        if not s:
            return 0
        else:
            if neg:
                if -int(s) < -2**31:
                    return -2**31
                else:
                    return -int(s)
            else:
                if int(s) > 2**31 - 1:
                    return 2**31 - 1
                else:
                    return int(s)