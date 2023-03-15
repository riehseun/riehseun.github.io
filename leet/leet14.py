class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for chars in zip(*strs):
            if all(char == chars[0] for char in chars):
                result += chars[0]
            else:
                return result

        return result