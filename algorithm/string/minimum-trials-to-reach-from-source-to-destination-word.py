"""
Given a dictionary of words, find minimum number of trials to reach from source word to destination word.

A valid trial on word 'w' is defined as either insert, delete or substitute operation of a single character in word 'w'
which results in a word 'w1' which is also present in the given dictionary.

For example, for dictionary {"BCCI","AICC","ICC","CCI","MCC","MCA", "ACC"}, minimum number of trials to reach from word "AICC" to "ICC" is 1.

Only 1 opeartion of deleting character 'A' is required to reach from word "AICC" to word "ICC".

Minimum number of trials to reach from "AICC" to "MCC" is 2(AICC->ICC->MCC) and minimum number of trials to reach from "AICC" to "MCA" is 3(AICC->ICC->MCC->MCA).

Now if you notice, there are no valid trials with source as "AICC" and destination as "BCCI" for above dictionary.

Hence the output returned by program should be '-1' indicating destination word cannot be reached from source word.

Usage:

	minimum-trials-to-reach-from-source-to-destination-word.py

"""

def run(count, source_word, destination_word, dictionary):
	"""
		Args:
			source_word:
			destination_word:
			dictionary:

		Returns:
			interger represeting # of trials (-1 representing impossible scenario)

	"""

	print(source_word +" vs "+ destination_word)
	if (source_word == destination_word):
		return count

	if (len(source_word) > len(destination_word)): # delete char
		left_over = source_word.replace(destination_word, "") # find out mismatches
		new_word = source_word.replace(left_over[0], "") # pick one mismatch and remove it

		if new_word not in dictionary:
			return -1
		else:
			new_count = count + 1
			return run(new_count, new_word, destination_word, dictionary)

	elif (len(source_word) < len(destination_word)): # insert char
		missing = destination_word.replace(source_word, "")
		new_word1 = missing[0] + source_word # try adding char at front
		new_word2 = source_word + missing[0] # try adding char at back
		new_word = ""
		if (len(destination_word.replace(new_word1, "")) < len(missing)): # if adding char at front is correct, length of string that is mismatching must decrease
			new_word = new_word1
		else:
			new_word = new_word2

		if new_word not in dictionary:
			return -1
		else:
			new_count = count + 1
			return run(new_count, new_word, destination_word, dictionary)

	else: # update char
		for i in range(0, len(source_word)):

			if (source_word[i] != destination_word[i]):
				new_word = source_word[0:i] + destination_word[i] + source_word[i+1:len(source_word)]
				if new_word not in dictionary:
					return -1
				else:
					new_count = count + 1
					return run(new_count, new_word, destination_word, dictionary)


assert(run(0, "AICC", "ICC", ["BCCI","AICC","ICC","CCI","MCC","MCA", "ACC"]) == 1)
assert(run(0, "ICC", "AICC", ["BCCI","AICC","ICC","CCI","MCC","MCA", "ACC"]) == 1)
assert(run(0, "AICC", "MCA", ["BCCI","AICC","ICC","CCI","MCC","MCA", "ACC"]) == 3)
assert(run(0, "AICC", "BCCI", ["BCCI","AICC","ICC","CCI","MCC","MCA", "ACC"]) == -1)