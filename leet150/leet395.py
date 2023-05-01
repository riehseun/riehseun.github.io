from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Find characters whose occurance is less than k
        # Find substrings that does not include those chars and meeting the
        # criteria of at least k repeating chars
        # Keep track of the length of those good substrings

        length_of_good_substring = {}
        # Time O(len(s)log(len(s)))
        self.subrouinte(s, k, length_of_good_substring)

        max_len = 0
        for key,val in length_of_good_substring.items():
            max_len = max(max_len, val)

        return max_len

    def subrouinte(self, s, k, length_of_good_substring):

        # Time O(len(s))
        # Space O(len(s))
        bad_chars = self.get_bad_chars(s, k)

        # The entire string is a good string.
        if not bad_chars:
            length_of_good_substring[s] = len(s)
            return

        start = 0

        for i in range(len(s)):
            # Check previous good string whenever hitting a bad char.
            if s[i] in bad_chars:
                if s[start:i] not in length_of_good_substring:
                    self.subrouinte(s[start:i], k, length_of_good_substring)

                start = i + 1

        # Check previous good string at the end.
        self.subrouinte(s[start:len(s)], k, length_of_good_substring)

    def get_bad_chars(self, s, k):

        char = defaultdict(int)

        for i in s:
            char[i] += 1

        bad_chars = set()

        for key,val in char.items():
            if val < k:
                bad_chars.add(key)

        return bad_chars