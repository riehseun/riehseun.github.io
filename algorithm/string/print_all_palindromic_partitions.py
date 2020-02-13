"""
Given a string, print all palindromic partitions of the given string.
Palindromic partitioning of a string is dividing the string into parts such that each part is a palindrome.

If abcb is a string, then
a-b-c-b and a-bcb will be palindormic partitions of the string.

a-b-cb, ab-cb, ab-c-b etc are partitions but not palindromic partitions of the string abcb.
b-c-b is palindromic but not a partition of the string abcb.

Example:

Input:
IDeserve
Output:
I-D-e-s-e-r-v-e
I-D-ese-r-v-e

Input:
banana
Output:
b-a-n-a-n-a
b-a-n-ana
b-a-nan-a
b-ana-n-a
b-anana

Usage:

    python print-all-parlindrom-partitions.py

"""


import math


def get_parlindrom_partitions(string):
	"""	Produces a list of parlindrom partitions of input string

	Args:
		string: string to be partitioned into substrings

	Returns:
		A list containing substring of the input string that are all parlindromes

	"""

	parlindromic_partitions = [] # list to store the result

	binary_array = []
	for i in range(0, int(math.pow(2, len(string)-1))):
		binary_array.append("")

	generate_binary_string(binary_array, 0, len(string)-1)
	print(binary_array)
	print(len(binary_array))

	count = 0
	for binary in binary_array:
		start_index_to_split = 0
		string_partition = []
		for index, value in enumerate(binary):
			if (value == "1"):
				string_partition.append(string[start_index_to_split:int(index+1)])
				start_index_to_split = int(index+1)
		string_partition.append(string[start_index_to_split:len(string)]) # append left-over substring after the last split
		count = count + 1
		if (is_everything_parlindrom(string_partition)):
			parlindromic_partitions.append(string_partition)

	return parlindromic_partitions


def generate_binary_string(array, start_index, number):
	""" populates input list with binaries where 0 represents - don't partition and 1 represents - partition

	Args:
		array: list to be populated with binaries
		start_index: index of array to start populating binaries from
		number: indicates that (2^number) of binaries should be generated

	Returns:
		list containing 2^(len(string)-1)) number of binaries
	"""

	if (number <= 0):
		return array

	number_of_binaries_to_generate = math.pow(2, number)
	number_of_binaries_to_generate = int(number_of_binaries_to_generate)

	for i in range(start_index, start_index + number_of_binaries_to_generate): # append 0 to the first half and 1 to the other half
		if (i<start_index + int(number_of_binaries_to_generate/2)):
			array[i] += "0"
		else:
			array[i] += "1"

	generate_binary_string(array, start_index, number-1) # recurse appending 0's and 1's for first half (sub-list)
	start_index =  start_index + int(number_of_binaries_to_generate/2) # updates start_index so that it starts from the beginning of second half
	generate_binary_string(array, start_index, number-1) # recurse appending 0's and 1's for second half (sub-list)


def is_everything_parlindrom(string_array):
	""" check if every element in the input list is parlindrom

	Args:
		string_array: list of strings

	Returns:
		bool indicating whether all string in the list is parlindrom or not
	"""

	for string in string_array:
		if (is_parlindrom(string) == False):
			return False
	return True


def is_parlindrom(string):
	""" check if string is parlindrom

	Args:
		string: input string to be checked if it is parlindrom

	Returns:
		bool indicating whether input string is parlindrom or not
	"""

	if (len(string) == 1): # single char is parlindrom
		return True

	if (len(string) % 2 == 0): # even number is not parlindrom
		return False

	string_index_to_check = int(len(string)/2-0.5) # only need to check half of index minus the middle char

	for i in range(string_index_to_check): # if asymmetry is found, return False
		if (string[i] != string[len(string)-1-i]):
			return False

	return True # passing above tests mean that string is symmetric, thus parlindrom


print (get_parlindrom_partitions("IDeserve"))
print (get_parlindrom_partitions("banana"))


assert (is_everything_parlindrom(["naban", "a"]) == True)
assert (is_everything_parlindrom(["naban", "nabanan"]) == False)
assert (is_everything_parlindrom(["I", "D", "ese", "r", "v", "e"]) == True)


assert (is_parlindrom("naban") == True)
assert (is_parlindrom("n") == True)
assert (is_parlindrom("nabanan") == False)
assert (is_parlindrom("nanana") == False)