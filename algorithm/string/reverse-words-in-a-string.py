"""
Given a string, reverse the string word by word.
Example:
String: "This is a string"
Output: "string a is This"

Usage:
	python reverse-words-in-a-string.py
"""


def run(string):
	"""
	Given a string, reverse the string word by word

	Args:
	string -- an input string

	Returns:
	reversed_string -- string whose words are at reversed order of the input string
	"""
	word_array = string.split(" ")

	reversed_word_array = []
	reversed_string = ""

	for word in word_array:
		reversed_word_array.append(word)

	while (len(reversed_word_array) != 0):
		reversed_string += reversed_word_array.pop()
		reversed_string += " "

	return reversed_string[:-1] # remove last space char


assert(run("This is a string") == "string a is This")