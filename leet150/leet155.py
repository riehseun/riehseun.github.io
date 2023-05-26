class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = math.inf

    def push(self, val: int) -> None:
        self.minimum = min(self.minimum, val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack:
            self.minimum = math.inf
        else:
            self.minimum = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()