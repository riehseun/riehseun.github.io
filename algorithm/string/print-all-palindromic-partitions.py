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

from itertools import combinations

def get_parlindrom_partitions(string):
	# breaking the input string into individual chars make it parlindome partition
	# for all partitioned sets of input string must be parlindrom
	# parlindrom is when either sub-string is a single char or symmetric with odd # of chars

	# placeholder for the result
	parlindromic_partitions = []

	# possible chunks of string division are 2,3,4,...,len(string). According number of index where division should take places are 1,2,3,...len(String)-1
	# for each number of index, find all possible partitions

	# case 0 division (4C0)
	# abcde

	# case 1 division (4C1)
	# a,bcde
	# ab,cde
	# abc,de
	# abcd,e

	# case 2 divisions (4C2)
	# a,b,cde
	# a,bc,de
	# a,bcd,e
	# ab,c,de
	# ab,cd,e
	# abc,d,e

	# case len(String)-2 divisions (4C1)
	# a,b,c,de
	# a,b,cd,e
	# a,bc,d,e
	# ab,c,d,e

	# case len(String)-1 divisions (4C0)
	# a,b,c,d,e

	# for each array containing partitioned sets of strings, add to result if is_everything_parlindrom() returns True
	for index in range(1, len(string)):
		combination_array = compute_combination(string, index)
		# print(is_everything_parlindrom(combination_array))
		print(combination_array)
		if(is_everything_parlindrom(combination_array)):
			parlindromic_partitions.append('-'.join(combination_array))
	return parlindromic_partitions

def compute_combination(string, number):
	"""takes a string and return an array containing combinations of chars of that string """
	combination_array = []
	if (number == 1):
		for index in range(1, len(string)):
			combination_array.append([string[:index],string[index:]])
	else:
		# come up with indexes where partitions can happen
		index_poistion = ""
		for digit in range(0, len(string)-1):
			index_poistion += str(digit)
		# print(index_poistion)

		for division_index_tuple in combinations(list(index_poistion), number):
			# print (division_index_tuple)
			temp_string_array = []

			for index in division_index_tuple:
				current_val = int(index)
				current_index = division_index_tuple.index(index)

				# if current index is first index
				if (current_index == 0):
					next_index = 1
					next_val = int(division_index_tuple[next_index])
					temp_string_array.append(string[:next_val])
				elif (current_index < len(division_index_tuple)-1):
					next_index = current_index + 1
					next_val = int(division_index_tuple[next_index])
					temp_string_array.append(string[current_val:next_val])
				# if current index is last index
				else:
					temp_string_array.append(string[current_val:])

			# print (temp_string_array)
			combination_array.append(temp_string_array)
	return combination_array

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
# print (get_parlindrom_partitions("banana"))

print (compute_combination("IDeserve", 7))
# print (compute_combination("IDeserve", 5))
print (compute_combination("IDeserve", 2))
print (compute_combination("IDeserve", 1))

assert (is_everything_parlindrom(["naban", "a"]) == True)
assert (is_everything_parlindrom(["naban", "nabanan"]) == False)
assert (is_everything_parlindrom(["I", "D", "ese", "r", "v", "e"]) == True)

assert (is_parlindrom("naban") == True)
assert (is_parlindrom("n") == True)
assert (is_parlindrom("nabanan") == False)
assert (is_parlindrom("nanana") == False)



