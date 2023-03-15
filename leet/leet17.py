class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Store the mapping between number and letter in a dictionary.
        mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        result = []

        # Base case.
        if len(digits) == 0:
            return []
        else:
            for char in mapping[digits[0]]:
                result.append(char)

        # Recursively compute all possible combinations.

        # Key idea: add each letter mathcing the current digit to all
        #           existing items in the resulting array.

        # Example
        # a b c
        # ad bd cd ae be ce af bf cf

        for digit in digits[1:]:
            result_old = result[:]
            for char in mapping[digit]:
                for item in result_old:
                    result.append(item+char)
            for item in result_old:
                result.remove(item)

        return result