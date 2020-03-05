"""
A DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: 'ACGAATTCCG'.
Write a function to find all the 10-letter-long sequences(sub-strings) that occur more than once in a DNA molecule.
Example - Input: 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT', Expected Output: [AAAAACCCCC,CCCCCAAAAA]

Usage:
	python find-10-letter-repeated-DNA-sequences.py
"""


def run(string):
	"""
	find all the 10-letter-long substring that occur more than once

	Args
	string -- an input string

	Returns
	sequences -- a list containing all the 10-letter-long substring that occur more than once
	"""
	sequences = []

	if (len(string) < 10):
		return sequences

	substring_array = []
	start_index = 0
	end_index = start_index + 10
	while (end_index <= len(string)):
		substring = ""
		for i in range(start_index, end_index):
			substring += string[i]
		substring_array.append(substring)
		start_index += 1
		end_index += 1

	seen = []
	for sequence in substring_array:
		if sequence in seen:
			sequences.append(sequence)
		else:
			seen.append(sequence)

	return sequences


assert(run('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT') == ["AAAAACCCCC","CCCCCAAAAA"])