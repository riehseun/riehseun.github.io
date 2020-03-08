"""
Given two strings S1 and S2. Find the longest common subsequence between S1 and S2.
Example: Input- S1 = "ACBEA" S2 = "ADCA"  Output- "ACA"

Usage:
	python longest-common-subsequence.py
"""


def run(s1, s2):
	"""
	Given two strings S1 and S2. Find the longest common subsequence between S1 and S2

	Args:
	s1 -- first input string
	s1 -- second input string

	Returns:
	subsequence -- longest common subsequence between s1 and s2
	"""
	subsequence = ""
	for char in s1:
		if char in s2:
			subsequence += char
	return subsequence


assert(run("ACBEA", "ADCA") == "ACA")