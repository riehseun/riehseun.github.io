class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for char in s:
            # If opening parenthesis, push to stack.
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                # If stack is not empty.
                if stack:
                    # If closing parenthesis
                    if char == ")" or char == "]" or char == "}":
                        # Pop if the top element is the corresponding
                        # opening parenthesis.
                        if ((char == ")" and stack[-1] == "(") or
                            (char == "]" and stack[-1] == "[") or
                            (char == "}" and stack[-1] == "{")):
                            # One of three conditions satisfied
                            stack.pop()
                        # If not, bracket mismatch
                        else:
                            return False
                # If expression does not start with (,[,{
                else:
                    return False

        # If stack is empty
        if not stack:
            return True

        return False