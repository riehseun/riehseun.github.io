class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in tokens:
            
            if not stack:
                stack.append(i)
                continue

            if i.lstrip("-").isdigit():
                stack.append(i)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == "+":
                    stack.append(str(a+b))
                if i == "-":
                    stack.append(str(a-b))
                if i == "*":
                    stack.append(str(a*b))
                if i == "/":
                    stack.append(str(int(float(a)/b)))
            
        return int(stack.pop())