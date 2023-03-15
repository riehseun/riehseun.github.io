class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        Find the longest palindrome substring.

        Args:
            s -- Input string

        Returns:
            The longest palindrome substring. (string)
        """

        longest_palindrome = ""

        # Time: O(n^2)
        # Space: O(1)
        for i in range(len(s)):

            # Example: "babad", "ccd" (odd case)
            palindrome_odd = self.find_longest_palindrome(i, i, s)

            # Example: "cbbd" (even case)
            palindrome_even = self.find_longest_palindrome(i, i+1, s)

            if len(palindrome_odd) < len(palindrome_even):
                palindrome = palindrome_even
            else:
                palindrome = palindrome_odd

            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome

        return longest_palindrome


    def find_longest_palindrome(self, a, b, s):
        """
        Find the longest palindrome substring who middle characters are
        a and b. (either a = b or a = b+1)

        Args:
            a -- An index postion of string s.
            b -- An index postion of string s.
            s -- Input string

        Return:
            The longest palindrome substring who middle characters are
            a and b.
        """

        # Time: O(n/2)
        # Space: O(1)
        while a >= 0 and b < len(s) and s[a] == s[b]:
            a -= 1
            b += 1

        return s[a+1:b]