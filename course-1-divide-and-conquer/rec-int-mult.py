# implementation of recursive approach to multiplying numbers as given in 'RecIntMult' algorithm

import math

def count_digits(input_number):
	if input_number == 0:
		return 1
	else:
		# log10 provides the power to raise 10 to in order to get the number, and floor rounds it to lowest integer
		return math.floor(math.log10(abs(input_number))) + 1

def rec_int_mult(x, y):
	
	# base case: check if the input numbers are single-digit and if so return their product directly
	if x < 10 and y < 10:
		return x * y
	
	# recursive case:
	else:
		# calculate n, the number of digits in x and y
		n_x = count_digits(x)
		n_y = count_digits(y)

		# split x into a and b, y into c and d
		a = x // (10**(n_x//2))
		b = x % (10**(n_x//2))
		c = y // (10**(n_y//2))
		d = y % (10**(n_y//2))

		# TODO: Implement the recursive multiplication here

print(rec_int_mult(24, 36))