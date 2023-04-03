class Solution:
    def romanToInt(self, s: str) -> int:

        # Dictionary to store symbol-value mapping
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000, "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}

        tokenize = []

        i = 0
        while i < len(s):
            if s[i] == "I" and i < len(s)-1:
                if s[i+1] == "V" or s[i+1] == "X":
                    tokenize.append(s[i:i+2])
                    i += 2
                    continue

            elif s[i] == "X" and i < len(s)-1:
                if s[i+1] == "L" or s[i+1] == "C":
                    tokenize.append(s[i:i+2])
                    i += 2
                    continue

            elif s[i] == "C" and i < len(s)-1:
                if s[i+1] == "D" or s[i+1] == "M":
                    tokenize.append(s[i:i+2])
                    i += 2
                    continue

            tokenize.append(s[i])
            i += 1

        result = 0
        for token in tokenize:
            result += roman[token]

        return result