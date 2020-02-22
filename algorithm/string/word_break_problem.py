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
		word_dictionary : a list containing words that are strings

	Returns:
		a bool indicating whether input string is breakable or not

	"""
	retVal = True

	substrings = get_sub_strings(string, word_dictionary)
	if (len(substrings) == 0):
		retVal = False
	elif (len(substrings) == 1):
	  	if (substrings == string):
			retVal = True
		else
			retVal = False
	else
		for word in substrings:
			"""break input string by word. apply get_sub_strings() on those two parts. recurse until substrings list is empty
			if broken part equals one of words, case True
			if substring list is empty, case False
			"""
			front_part = string.split(word)[0]
			# print("front")
			# print(front_part)
			back_part = string.split(word)[1]
			# print("back")
			# print(back_part)
			print("split by: " + word)
			if (front_part != ""):
			    if (front_part not in word_dictionary):
					print("checking front: " + front_part)
					is_string_breakable(front_part, word_dictionary)


			if (back_part != ""):
			    if (back_part not in word_dictionary):
					print("checking back: " + back_part)
					is_string_breakable(back_part, word_dictionary)

	return retVal


def get_sub_strings(string, word_dictionary):
	"""

	Args:
		string : a string
		word_dictionary : a list containing words that are strings

	Returns:
		a list of strings from word_dictionary that are sub-strings of input string


	"""
	substrings = []

	for word in word_dictionary:
		if word in string:
			substrings.append(word)
	return substrings


word_dictionary = ["arrays", "dynamic", "heaps", "IDeserve", "learn", "learning", "linked", "list", "platform", "programming", "stacks", "trees"]
assert(is_string_breakable("IDeservelearningplatform", word_dictionary) == True)
# assert(is_string_breakable("dynamic", word_dictionary) == True)
# assert(is_string_breakable("arraysprogramminglist", word_dictionary) == True)
# assert(is_string_breakable("listprogrammingheap", word_dictionary) == False)
# assert(is_string_breakable("love", word_dictionary) == False)

