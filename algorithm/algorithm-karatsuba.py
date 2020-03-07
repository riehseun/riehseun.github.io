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
		print("OUCH")
		return

	# split both operands by half
	firsthalf_operand1 = operand1[:int(len(operand1)/2)]
	secondhalf_operand1 = operand1[int(len(operand1)/2):len(operand1)]
	firsthalf_operand2 = operand2[:int(len(operand2)/2)]
	secondhalf_operand2 = operand2[int(len(operand2)/2):len(operand2)]

	result = 0
	if (len(operand1) == 2 and len(operand2) == 2):
		ac = int(firsthalf_operand1) * int(firsthalf_operand2)
		bd = int(secondhalf_operand1) * int(secondhalf_operand2)
		ad = int(firsthalf_operand1) * int(secondhalf_operand2)
		bc = int(secondhalf_operand1) * int(firsthalf_operand2)
		return (ac * 100) + bd + (ad + bc) * 10

	ac = run(firsthalf_operand1, firsthalf_operand2)
	bd = run(secondhalf_operand1, secondhalf_operand2)
	ad = run(firsthalf_operand1, secondhalf_operand2)
	bc = run(secondhalf_operand1, firsthalf_operand2)

	# print(int((ac * math.pow(10, len(operand1)))))
	#print(int((ac * math.pow(10, len(operand1)))))
	#print(str(ac) + " -- " + str(math.pow(10, len(operand1))))
	#print(int((ac * math.pow(10, len(operand1)))))
	#print(str(ac * 10000000000000000))
	#print(math.pow(10, len(operand1)))
	ac_in_str = str(ac)
	for i in range(0, len(operand1)):
		ac_in_str += "0"
	ad_plus_bc_in_str = str(ad+bc)
	for i in range(0, int(len(operand1)/2)):
		ad_plus_bc_in_str += "0"

	result = int(ac_in_str) + bd + int(ad_plus_bc_in_str)
	return result


assert(run("5678", "1234") == 7006652)
assert(run("12345678", "12345678") == 152415765279684)
assert(run("74639573", "94756283") == 7072568502187159)
assert(run("8475637284756461", "7483726374837363") == 63429350291486860416277938452343)
assert(run("3141592653589793238462643383279502884197169399375105820974944592", "2718281828459045235360287471352662497757247093699959574966967627") == 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184)


