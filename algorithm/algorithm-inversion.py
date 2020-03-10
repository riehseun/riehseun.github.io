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
	Integer representing the number of inversion
	"""
	if filepath != "":
		with open(filepath, 'r') as line:
			integer_array = line.read().split("\n")

	# print(len(integer_array))

	# base case (only two element in each array)

	if len(integer_array) == 1:
		return integer_array

	if len(integer_array) == 2:
		if int(integer_array[0]) > int(integer_array[1]):
			temp = integer_array[0]
			integer_array[0] = integer_array[1]
			integer_array[1] = temp
		return integer_array


	first_half = integer_array[:int(len(integer_array)/2)]
	second_half = integer_array[int(len(integer_array)/2):len(integer_array)]

	sorted_first_half = run(first_half, "")
	sorted_second_half = run(second_half, "")

	print(sorted_first_half)
	print(sorted_second_half)
	# integer_array = sorted_first_half + sorted_second_half
	sorted_integer_array = []
	i = 0
	j = 0
	while i < len(first_half) and j < len(second_half):
		if int(first_half[i]) < int(second_half[j]):
			sorted_integer_array.append(first_half[i])
			i += 1
		else:
			sorted_integer_array.append(second_half[j])
			j += 1

	integer_array = sorted_integer_array
	return integer_array



print(run([], "simple.txt"))
# print(run([], "test.txt"))
# print(run([], "algorithm-inversion.txt"))