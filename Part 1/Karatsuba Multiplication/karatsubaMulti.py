# Version 3.6

def karatsuba(x, y):
	'''
	Recursive function to compute multiplication of large numbers.
	Input: Two numbers x and y, can be of uneven length
	Output: Multiplication of x and y.
	'''
	x_len = len(str(x))
	y_len = len(str(y))
	n = max(x_len, y_len) # if no. of digits is uneven

	# Base Case, normal multiplication if # of digits is 1
	if x_len == 1 or y_len == 1:
		return x*y

	# Dividing x and y into a,b and c,d
	a = x // 10**(n//2) #First half
	b = x % 10**(n//2) #Second half

	c = y // 10**(n//2) #First half
	d = y % 10**(n//2) #Second half

	# 3 Recurrences:
	R1 = karatsuba(a, c)
	R2 = karatsuba(b, d)
	R3_ = karatsuba(a+b, c+d)
	R3 = R3_ - R2 - R1

	# Returning 10^n(a*c) + 10^(n/2)(ad + bc) + bd
	return int(R1*10**(n) + R3*10**(n//2) + R2)
