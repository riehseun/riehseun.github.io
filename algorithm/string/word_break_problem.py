"""
Given a dictionary of words and a string of characters, find if the string of characters can be broken into individual valid words from the dictionary.

Example:
Dictionary: arrays, dynamic, heaps, IDeserve, learn, learning, linked, list, platform, programming, stacks, trees

String    : IDeservelearningplatform
Output   : true

Because the string can be broken into valid words: IDeserve learning platform

Usage:

	word_break_problem.py

"""


def is_string_breakable(string, word_dictionary):
	"""Checks if string can be broken into words from the dictionary

	Args:
		string : a string
		word_dictionary : a list containing words

	Returns:
		a bool indicating whether input string is breakable or not

	"""


word_dictionary = ["arrays", "dynamic", "heaps", "IDeserve", "learn", "learning", "linked", "list", "platform", "programming", "stacks", "trees"]
assert(is_string_breakable("IDeservelearningplatform", word_dictionary) == True)
assert(is_string_breakable("arraysprogramminglist", word_dictionary) == True)
assert(is_string_breakable("listprogrammingheap", word_dictionary) == False)

