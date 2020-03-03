"""
Given a string, find all the permutations of the string.
For example:
Input String: abc
Output: {bca, acb, abc, cba, bac, cab}

Usage:
	python all-permutations-of-a-string.py
"""


def run(string, permutations, index):
	"""
	Given a string, find all the permutations of the string

	Args:
	string -- an input string

	Returns:
	permutations -- list containing all the permutations of the input string
	"""

	if (len(string) == 0):
		return permutations

	n = len(string)
	n_factorial = 1
	while (n > 0):
		n_factorial *= n
		n -= 1

	if (len(permutations) == 0):
		m = n_factorial
		while (m > 0):
			permutations.append("")
			m -=1

	# print(permutations)
	# print(permutations[0])

	range_for_each_char = int(n_factorial / len(string))
	print(range_for_each_char)
	start_index = index
	end_index = range_for_each_char
	for char in string:
		for k in range(start_index, end_index):
			# print(str(start_index) + " to " + str(end_index))
			# print(k)
			permutations[k] += char
		start_index += range_for_each_char
		end_index += range_for_each_char
	print(permutations)

	for i in range(0, len(string)): # there are len(string) sub-problems
		return run(string.replace(string[i], ""), permutations, (i+1)*range_for_each_char)


print(run("abcd", [], 0))