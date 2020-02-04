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
"""

def get_parlindrom_partitions(string):
	# breaking the input string into individual chars make it parlindome partition
	# for all partitioned sets of input string must be parlindrom
	# parlindrom is when either sub-string is a single char or symmetric with odd # of chars

	# placeholder for the result
	parlindromic_partitions = []

	# Generate 2^len(string) binaries where 0 = don't partition and 1 = partition. Store them into an array. Then split strings based on 1s'
	# Create an array of size 2^len(strong)-1 of empty strings. For half of element, add 0. For the other half, add 1. Use recursion to apply this rule
	binary_array = []
	for i in range(2^len(string)-1):
		binary_array.append("")

	generate_binary_string(binary_array, 0, len(string))

	print(binary_array)

	for binary in binary_array:
		start_index_to_split = 0
		string_partition = []
		for digit in binary:
			if (digit == 1):
				string_partition.append(string[start_index_to_split:indexOf(digit)])
				start_index_to_split = indexOf(digit) + 1
		if (is_everything_parlindrom(string_partition)):
			parlindromic_partitions.append(string_partition)

	return parlindromic_partitions

def generate_binary_string(array, start_index, number):
	""" takes a number and array. generate binaries into array """
	if (number <= 0):
		return array

	number_of_binaries_to_generate = 2^number

	for (i=start_index; i<number_of_binaries_to_generate; i++):
		if (i<number_of_binaries_to_generate/2):
			array[i] += "0"
		else:
			array[i] += "1"

	generate_binary_string(array, 0, number-1) # generate for first half
	generate_binary_string(array, number_of_binaries_to_generate/2, number-1) # generate for second half

def is_everything_parlindrom(string_array):
	""" takes an array of strings and return true if all elements in the array are parlindroms """
	for string in string_array:
		if (is_parlindrom(string) == False):
			return False
	return True

def is_parlindrom(string):
	""" takes a string and return true if it is parlindrom """

	# single char is parlindrom
	if (len(string) == 1):
		return True

	# even number is not parlindrom
	if (len(string) % 2 == 0):
		return False

	# only need to check half of index minus the middle char
	string_index_to_check = int(len(string)/2-0.5)

	# if asymmetry is found, return False
	for i in range(string_index_to_check):
		if (string[i] != string[len(string)-1-i]):
			return False

	# passing above test means string is symmetric
	return True

# print (get_parlindrom_partitions("IDeserve"))
print (get_parlindrom_partitions("banana"))

assert (is_everything_parlindrom(["naban", "a"]) == True)
assert (is_everything_parlindrom(["naban", "nabanan"]) == False)
assert (is_everything_parlindrom(["I", "D", "ese", "r", "v", "e"]) == True)

assert (is_parlindrom("naban") == True)
assert (is_parlindrom("n") == True)
assert (is_parlindrom("nabanan") == False)
assert (is_parlindrom("nanana") == False)