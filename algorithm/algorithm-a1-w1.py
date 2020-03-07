"""
Usage:
	python algorithm-a1-w1.py
"""


import math
def run(operand1, operand2):
	"""
	performs Karatsuba multiplication

	Args:
	operand1 -- string representing the first operand of multiplication
	operand2 -- string representing the second operand of multiplication

	Returns:
	result -- integer representing the result of multiplication
	"""

	# error case
	if (len(operand1) < 2 or len(operand1) < 2):
		return -1

	# split both operands by half
	firsthalf_operand1 = operand1[:int(len(operand1)/2)]
	secondhalf_operand1 = operand1[int(len(operand1)/2):len(operand1)]
	firsthalf_operand2 = operand1[:int(len(operand2)/2)]
	secondhalf_operand2 = operand1[int(len(operand2)/2):len(operand2)]

	result = 0
	if (len(operand1) == 2 and len(operand2) == 2):
		one = int(firsthalf_operand1) * int(firsthalf_operand2)
		two = int(secondhalf_operand1) * int(secondhalf_operand2)
		three = (int(firsthalf_operand1) + int(secondhalf_operand1)) * (int(firsthalf_operand2) + int(secondhalf_operand2))
		one = one * 100
		three = three * 10
		result = one + two + three
		return str(result)

	one = run(firsthalf_operand1, firsthalf_operand2)
	two = run(secondhalf_operand1, secondhalf_operand2)
	three = (int(firsthalf_operand1) + int(secondhalf_operand1)) * (int(firsthalf_operand2) + int(secondhalf_operand2))
	one = one * math.pow(10, int(len(operand1)))
	three = three * math.pow(10, int(len(operand1)/2))
	result = one + two + three
	return str(result)


run("3141592653589793238462643383279502884197169399375105820974944592", "2718281828459045235360287471352662497757247093699959574966967627")