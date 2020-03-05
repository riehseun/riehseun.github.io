"""
Given a string, find all the permutations of the string.
For example:
Input String: abc
Output: {bca, acb, abc, cba, bac, cab}

Usage:
	python all-permutations-of-a-string.py
"""


def run(string, index):
	result_array = []
	compute_permutation(string, result_array, index)
	return result_array


def compute_permutation(string, permutations, index):
	"""
	Given a string, find all the permutations of the string

	Args:
	string -- an input string

	Returns:
	permutations -- list containing all the permutations of the input string
	"""

	# base case
	if (len(string) == 0):
		return permutations

	# calculate factorial
	n = len(string)
	n_factorial = 1
	while (n > 0):
		n_factorial *= n
		n -= 1

	# if first interation, populate result array with empty string
	if (len(permutations) == 0):
		m = n_factorial
		while (m > 0):
			permutations.append("")
			m -=1

	range_for_each_char = int(n_factorial / len(string))
	start_index = index
	end_index = index + range_for_each_char

	for char in string:
		for k in range(start_index, end_index):
			permutations[k] += char
		start_index += range_for_each_char
		end_index += range_for_each_char

	for i in range(0, len(string)): # there are len(string) sub-problems
		compute_permutation(string.replace(string[i], ""), permutations, index+i*range_for_each_char)


def is_there_duplicate_item(array):
	if (len(array) == len(set(array))):
		return False
	else:
		return True


assert(is_there_duplicate_item(["abcd", "abdc", "acdb", "adcb"]) == False)
assert(is_there_duplicate_item(["abcd", "abdc", "acdb", "acdb"]) == True)
assert(is_there_duplicate_item(run("abcd", 0)) == False)

