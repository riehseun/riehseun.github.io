"""
Given two strings S1 and S2. Find the longest common substring between S1 and S2.
Example: S1 = "LCLC"  S2 = "CLCL"  LCS = "CLC"

Usage:
	python longest-common-substring.py
"""


def run(s1, s2):
	"""
	longest common substring between S1 and S2

	Args:
	s1 -- first input string
	s2 -- second input string

	Returns:
	s3 - longest common substring between S1 and S2
	"""

	longest_conmon_substring = ""
	# consecutive words that are substrings of the longer string can be found by remove chars from beginning and end
	if s1 > s2:
		for i in range(1, len(s1)):
			if s1[:-i] in s2:
				if (len(s1[:-i]) > len(longest_conmon_substring)): # remove i chars from the end
					longest_conmon_substring = s1[:-i]
			if s1[i:len(s1)] in s2:
				if (len(s1[i:len(s1)]) > len(longest_conmon_substring)): # remove i chars from the beginning
					longest_conmon_substring = s1[i:len(s1)]
	else:
		for i in range(1, len(s2)):
			if s2[:-i] in s1:
				if (len(s2[:-i]) > len(longest_conmon_substring)):
					longest_conmon_substring = s2[:-i]
			if s2[i:len(s1)] in s1:
				if (len(s2[i:len(s1)]) > len(longest_conmon_substring)):
					longest_conmon_substring = s2[i:len(s1)]
	return longest_conmon_substring


assert(len(run("LCLC", "CLCL")) == 3)