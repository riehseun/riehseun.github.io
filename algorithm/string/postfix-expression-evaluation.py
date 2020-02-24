"""
valuate the value of a Postfix expression, also known as expression in Reverse Polish Notation.
Given: An array of strings, every string being either an operand or an operator, in Reverse Polish Notation, find out the value of the expression.

Assumptions: The given postfix expression will be a valid expression.
1. String operands will be valid Integers (positive or negative)
2. Operators will be valid operators in: + - / *
3. 0 will not be passed as a divisor for division operation.

Example:
Input:
20    30    +
Output:
50

Input:
5    1    2    +    4    *    +    3    -
Output:
14

Note: Input is an array of strings to allow numbers with multiple digits as operands.
For example "20", "45" etc

Usage:

    postfix_expression_evaluation.py

"""


def evaulte(list_of_string):
	"""evlautes postfix expression

	Args:
		list_of_string: list of strings

	Returns:
		number, which is the result of evaluating postfix expression

	"""

	stack = []

	for item in list_of_string:
		if (item.isnumeric()):
			stack.append(item)
		else:
			if (item == "+"):
				b = float(stack.pop())
				a = float(stack.pop())
				c = a + b
				stack.append(c)
			elif (item == "-"):
				b = float(stack.pop())
				a = float(stack.pop())
				c = a - b
				stack.append(c)
			elif (item == "*"):
				b = float(stack.pop())
				a = float(stack.pop())
				c = a * b
				stack.append(c)
			elif (item == "/"):
				b = float(stack.pop())
				a = float(stack.pop())
				c = a / b
				stack.append(c)
			else:
				return "Invalid Operator"

	return stack.pop()


assert(evaulte(["5", "1", "2", "+", "4", "*", "+", "3", "-"]) == 14)