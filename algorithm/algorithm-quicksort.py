"""
	Usage: python algorithm-quicksort.py
"""

def run(integer_array, filepath):
	"""
	Implements quicksort and computes # of comparison in partition subroutine

	Args:
	integer_array -- list of integers
	file -- string representing location of files containing lots of number

	Retunrs:
	Tuple of list representing sorted array and an integer representing the number of comparison in partition subroutine
	"""

	if filepath != "":
		with open(filepath, 'r') as line:
			integer_array = line.read().split("\n")

	# base case
	if len(integer_array) == 1:
		# return (integer_array, num_comparison)
		return integer_array

	pivot = choose_pivot(integer_array)

	partitioned_integer_array = partition(integer_array, pivot)
	print(partitioned_integer_array)

	partition_index = partitioned_integer_array.index(pivot)
	first_partition = partitioned_integer_array[0:partition_index]
	second_partition = partitioned_integer_array[partition_index:len(partitioned_integer_array)]

	run(first_partition, "")
	run(second_partition, "")

	return partitioned_integer_array


def partition(integer_array, pivot):
	"""
	Partitions an array around pivot into two sub arrays

	Args:
	integer_array -- list of integers
	pivot -- element of array at which partition takes place

	Returns:
	a list after the partition around pivot
	"""

	i = 0
	for j in range(0, len(integer_array)):
		if integer_array[j] < pivot and integer_array != pivot:
			temp = integer_array[i]
			integer_array[i] = integer_array[j]
			integer_array[j] = temp
			i += 1

	temp = integer_array[0]
	integer_array[0] = integer_array[i-1]
	integer_array[i-1] = temp

	return integer_array


def choose_pivot(integer_array):
	"""
	Choose a pivot elemnet from input list

	Args:
	integer_array -- list of integers

	Retunrs:
	Tuple of an integer and an index representing the pivot
	"""

	return integer_array[0]

	# return integer_array[len(integer_array)-1]

	# return


print(run([], "test.txt"))
# print(run([], "algorithm-quicksort.txt"))