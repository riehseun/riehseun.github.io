class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        # Number of dots should be exactly 3.
        # When we take 2 or 3 letters make sure first letter shouldn't be zero.
        # We can only take any number from 0-255.

        # Take 1 number.
        # Take 2 number but also check if first digit is 0.
        # Take 3 number but also check if first digit is 0 and number exceeds 255.
        result = set()
        self.helper(0, s, 0, "", result)
        return result

    def helper(self, i, s, num_dots, string, result):

        if i >= len(s):
            if num_dots > 3:
                string = string[:-1]
            if string[-1] != ".":
                result.add(string)
            return

        if num_dots > 3:
            return

        new_string = string + s[i] + '.'
        self.helper(i+1, s, num_dots+1, new_string, result)

        if s[i] != "0":
            new_string = string + s[i:i+2] + '.'
            self.helper(i+2, s, num_dots+1, new_string, result)

        if s[i] != "0" and int(s[i:i+3]) <= 255:
            new_string = string + s[i:i+3] + '.'
            self.helper(i+3, s, num_dots+1, new_string, result)