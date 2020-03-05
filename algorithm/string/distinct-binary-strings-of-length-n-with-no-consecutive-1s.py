"""
Count all possible distinct binary strings of length n with no consecutive 1s

Usage:
	python distinct-binary-strings-of-length-n-with-no-consecutive-1s.py
"""


import math
def run(n):
	"""
	Count all possible distinct binary strings of length n with no consecutive 1s

	Args:
	n -- length of binary

	Returns:
	number of distinct binary strings with no consecutive 1s
	"""

	# number of binary string of lenth n is 2 ^ n
	# 1's cannot constitue more than half or 0's should at least be half Ex. 01010101, 10101010
	# number of 1 can be between 0 and lenth(n). Only valid cases would be 0, 1, 2, ... , length(n)/2. [length(n)/2]+1, [length(n)/2]+2], ... , length(n) are not valid
	# So (2 ^ n) /2 is the answer
	return math.pow(2, n) / 2


assert(run(4) == 8)