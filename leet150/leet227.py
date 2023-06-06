class Solution:
    def calculate(self, s: str) -> int:

        s = s.replace(" ", "")
        stack = []
        num = 0
        operator = "+"

        for i, token in enumerate(s):

            if token.isdigit():
                num = num*10 + int(token)

            elif token in "+-*/":
                self.helper(stack, operator, num)
                num = 0
                operator = token

        self.helper(stack, operator, num)
        return sum(stack)

    def helper(self, stack, operator, num):

        if operator == "+":
            stack.append(num)
        if operator == "-":
            stack.append(-num)
        if operator == "*":
            stack.append(stack.pop()*num)
        if operator == "/":
            stack.append(int(stack.pop()/num))