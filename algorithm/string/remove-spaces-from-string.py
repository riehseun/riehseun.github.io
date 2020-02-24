"""
Given a string of characters consisting of 0 or more spaces, remove all the spaces from this given string.

Separation of spaces from other characters should be done in-place(without using extra space). Expected time complexity is O(n).

For example, if the input string is "  Hi, How are you?  " then the output returned should be "Hi,Howareyou?"

Usage:

    remove_spaces_from_string.py

"""


def execute(string):
	"""Removes all speaces from input string and return it

	Args:
		string: a string

	Returns:
		a string without any space

	"""
	string_without_space = ""

	for char in string:
		if (char != " "):
			string_without_space += char

	return string_without_space


assert(execute("  Hi, How are you?  ") == "Hi,Howareyou?")