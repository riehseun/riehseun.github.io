class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]

        output = [[1], [1,1]]

        for _ in range(2, numRows):
            new_array = []
            last_array = output[-1]

            new_array.append(last_array[0])
            for i in range(len(last_array)-1):
                new_array.append(last_array[i]+last_array[i+1])
            new_array.append(last_array[len(last_array)-1])

            output.append(new_array)

        return output