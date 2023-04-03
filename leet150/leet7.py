class Solution:
    def reverse(self, x: int) -> int:

        is_neg = False
        x = str(x)

        if x[0] == "-":
            x = x[1:]
            is_neg = True

        arr = []
        for i in x:
            arr.append(i)

        start = 0
        end = len(x)-1

        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1

        result = "".join(arr)

        if is_neg:
            if -int(result) < -2**31:
                return 0
            else:
                return -int(result)
        else:
            if int(result) > 2**31 - 1:
                return 0
            else:
                return int(result)