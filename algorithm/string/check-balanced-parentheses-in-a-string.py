"""
Given a string with parentheses (round brackets) and letters, validate the parentheses:
1. An opening parentheses '(' should have a closing matching parentheses ')'.
2. Closing matching parentheses should not come before an opening parentheses.
Note: Assume that the string has alphabets and numbers and round brackets only.

For example:
((BCD)AE) - Valid
)(PH)N(X) - Invalid

Usage:
	check-balanced-parentheses-in-a-string.py
"""

def run(string):
	"""
	Validates that parentheses are place corrected in a given string

	Args:
		string -- input string

	Returns:
		bool indicating if string has valid parentheses or not
	"""
	count_left_parentheses = 0
	count_right_parentheses = 0

	for char in string:
		if (char == "("):
			count_left_parentheses += 1
		elif (char == ")"):
			count_right_parentheses += 1

		if (count_right_parentheses > count_left_parentheses): # closinng matching parenthese come before an opening parentheses
			return False

	if (count_left_parentheses == count_right_parentheses):
		return True
	else:
		return False


assert(run("((BCD)AE)") == True)
assert(run(")(PH)N(X)") == False)