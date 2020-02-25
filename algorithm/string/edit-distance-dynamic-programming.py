"""

Minimum Edit distance between two strings str1 and str2 is defined as the minimum number of insert/delete/substitute operations required to transform str1 into str2.

For example if str1 = "ab", str2 = "abc" then making an insert operation of character 'c' on str1 transforms str1 into str2.

Therefore, edit distance between str1 and str2 is 1. You can also calculate edit distance as number of operations required to transform str2 into str1.

For above example, if we perform a delete operation of character 'c' on str2, it is transformed into str1 resulting in same edit distance of 1.

Looking at another example, if str1 = "INTENTION" and str2 = "EXECUTION", then the minimum edit distance between str1 and str2 turns out to be 5

All operations are performed on str1.

Credits for above example: Stanford University (https://web.stanford.edu/class/cs124)

Given two strings, write a program to find out the minimum edit distance between them.

Usage:

	edit-distance-dynamic-programming.py

"""

def run(count, source_word, destination_word):
	"""
	Calculates minimum edit distnace

	Args:


	Returns:


	"""
	if (source_word == destination_word):
		return count

	if (len(source_word) > len(destination_word)): # delete char
		left_over = source_word.replace(destination_word, "") # find out mismatches
		new_word = source_word.replace(left_over[0], "") # pick one mismatch and remove it
		new_count = count + 1
		return run(new_count, new_word, destination_word)

	elif (len(source_word) < len(destination_word)): # insert char
		missing = destination_word.replace(source_word, "")
		new_word1 = missing[0] + source_word # try adding char at front
		new_word2 = source_word + missing[0] # try adding char at back
		new_word = ""
		if (len(destination_word.replace(new_word1, "")) < len(missing)): # if adding char at front is correct, length of string that is mismatching must decrease
			new_word = new_word1
		else:
			new_word = new_word2

		new_count = count + 1
		return run(new_count, new_word, destination_word)

	else: # update char
		for i in range(0, len(source_word)):

			if (source_word[i] != destination_word[i]):
				new_word = source_word[0:i] + destination_word[i] + source_word[i+1:len(source_word)]
				new_count = count + 1
				return run(new_count, new_word, destination_word)


assert(run(0, "ab", "abc") == 1)
assert(run(0, "INTENTION", "EXECUTION") == 5)