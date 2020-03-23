"""
Usage: python algorithm-inversion.py
"""


def run(integer_array, filepath):
	"""
	Implements merge sort and computes # of inversion

	Args:
	integer_array -- list of integers
	file -- string representing location of files containing lots of number

	Retunrs:
	Tuple of list representing sorted array and an integer representing the number of inversion
	"""

	if filepath != "":
		with open(filepath, 'r') as line:
			integer_array = line.read().split("\n")

	# base case (only one or two elements in each array)
	if len(integer_array) == 1:
		num_inversion = 0
		return (integer_array, num_inversion)

	if len(integer_array) == 2:
		num_inversion = 0
		if int(integer_array[0]) > int(integer_array[1]):
			temp = integer_array[0]
			integer_array[0] = integer_array[1]
			integer_array[1] = temp
			num_inversion = 1
		return (integer_array, num_inversion)

	first_half = integer_array[:int(len(integer_array)/2)]
	second_half = integer_array[int(len(integer_array)/2):len(integer_array)]

	result_from_first_half = run(first_half, "")
	result_from_second_half = run(second_half, "")

	sorted_first_half = result_from_first_half[0]
	sorted_second_half = result_from_second_half[0]
	num_inversion_first_half = result_from_first_half[1]
	num_inversion_second_half = result_from_second_half[1]

	i = 0
	j = 0
	sorted_integer_array = []
	num_inversion = num_inversion_first_half + num_inversion_second_half
	for k in range(0, len(integer_array)):
		if int(sorted_first_half[i]) < int(sorted_second_half[j]):
			sorted_integer_array.append(sorted_first_half[i])
			if i < len(sorted_first_half)-1:
				i += 1
			# if finished with one array, just push elements of other sorted array
			else:
				for index in range(j, len(sorted_second_half)):
					sorted_integer_array.append(sorted_second_half[index])
				break
		else:
			sorted_integer_array.append(sorted_second_half[j])
			# count inversion
			num_inversion += len(sorted_first_half[i:len(sorted_first_half)])

			if j < len(sorted_second_half)-1:
				j += 1
			# if finished with one array, just push elements of other sorted array
			else:
				for index in range(i, len(first_half)):
					sorted_integer_array.append(sorted_first_half[index])
				break

	return (sorted_integer_array, num_inversion)


print(run([], "algorithm-inversion.txt")[1])