"""
Given an array of strings, sort the array in such a way that all anagrams are grouped together.

For example, if the given array input is {"abcd","abc","abce", "acd","abdc"} then output array should be {"abc","abcd","abdc","abce","acd"}.

Note that order among non-anagram strings is not important here.

Instead of returning above array as output, your program could have returned an array having different order of strings
but strings "abcd" and "abdc" must be placed next to each other with no specific ordering requirement among them.

So the output array - {"abdc","abcd","abc","abce","acd"} would also be a correct output.

Usage:

	group-all-anagrams-together-set-1.py

"""


def run(array):
	"""
	Reorders input array so that anagrams are side by side

	Args:
		array : a list containing strings

	Returns:
		a list containing strings where anagrams are grouped together


	"""

	return_array = []

	taken = [] # list of strings taken as anagramg
	storage = [] # list of list containing anagrams

	for string in array: # take a first string
		anagrams_group = []
		anagrams_group.append(string)
		for anagrams_candidate in array: # compare all strings against the first string
			if (string != anagrams_candidate and is_anagram(string, anagrams_candidate) and string not in taken): # string must not be itself, and not already identified as an anagram of another string
				anagrams_group.append(anagrams_candidate)
				taken.append(anagrams_candidate)
		if (string not in taken):
			storage.append(anagrams_group)


	for list_item in storage:
		for string in list_item:
			return_array.append(string)

	return return_array


def is_anagram(string1, string2):
	"""
	check if two strings are anagrams

	Args:
		string1: first string
		string2: second string

	Returns:
		bool indicating whether two strings are anagrams or not

	"""

	if (len(string1) != len(string2)):
		return False

	for char in string1:
		if (char not in string2):
			return False

	return True


assert(is_anagram("abdc", "abdc") == True)
assert(is_anagram("abdc", "abce") == False)
assert(is_anagram("abc", "abce") == False)
print(run(["abcd","abc","abce", "acd","abdc"]))