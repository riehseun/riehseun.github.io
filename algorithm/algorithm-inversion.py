"""
This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the i^{th}i
th
  row of the file indicates the i^{th}i
th
  entry of an array.

Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.

The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.

(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or your own devising. Then post your best test cases to the discussion forums to help your fellow students!]
"""

def run(integer_array, filepath):
	"""
	Computes # of inversion

	Args:
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