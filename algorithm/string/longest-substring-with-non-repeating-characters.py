"""
Given a string, find the longest substring with non-repeating characters.
Example:
Input : ABCDABDEFGCABD
Output: ABDEFGC

Usage:

	longest-substring-with-non-repeating-characters.py

"""


def run(string):
	"""

	Given a string, find the longest substring with non-repeating characters

	Args:
		string : an input string

	Returns:
		a string that is the longest substring with non-repeating characters


	"""

	non_repeating_substrings = ""

	for i in range(0, len(string)):
		substring = string[i]
		for char in string[i+1:len(string)]:
			if (char not in substring):
				substring += char
			else:
				break
		if (len(substring) > len(non_repeating_substrings)):
			non_repeating_substrings = substring

	return non_repeating_substrings


assert(run("ABCDABDEFGCABD") == "ABDEFGC")