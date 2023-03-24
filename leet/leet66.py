class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for num in digits:
            string += str(num)

        integer = int(string) + 1
        string = str(integer)

        result = []
        for char in string:
            result.append(int(char))

        return result