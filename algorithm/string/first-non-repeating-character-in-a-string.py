"""
Find the first non repeating character in string.
Example:
Input : ADBCGHIEFKJLADTVDERFSWVGHQWCNOPENSMSJWIERTFB
Output: K

Usage:
	python first-non-repeating-character-in-a-string.py
"""


def run(string):
	"""
	Find the first non repeating character in string

	Args:
		string -- an input string

	Returns:
		string[i] -- first non repeating character in string
	"""

	for i in range(0, len(string)):
		string_to_check = string[0:i] + string[i+1:len(string)]
		if (string[i] not in string_to_check):
			return string[i]


assert(run("ADBCGHIEFKJLADTVDERFSWVGHQWCNOPENSMSJWIERTFB") == "K")