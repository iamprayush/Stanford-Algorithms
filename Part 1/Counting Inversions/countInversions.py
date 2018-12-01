# Version 3.6

def countInv(arr):
	"""
	Counts the number of inversions in a given array
	by divide and conquer approach.
	Input : array
	Output : Tuple containing (sorted array, # of inversions)
	"""

	# Base Case
	if len(arr) == 1:
		return arr, 0

	else:
		mid = int(len(arr)//2)
		a = arr[:mid]
		b = arr[mid:]
		
		# Recursively split array into 2 equal parts and count left and right invs
		a, ai = countInv(a)
		b, bi = countInv(b)
		c = []

		i = 0
		j = 0
		invs = ai + bi + 0 # invs in left half + invs in right half + split invs(initially 0)

		while i < len(a) and j < len(b):
			if a[i] < b[j]:
				c.append(a[i])
				i += 1
			elif b[j] < a[i]:
				c.append(b[j])
				j += 1
				invs += len(a) - i # counting split inversions

		c += a[i:] + b[j:]

	return c, invs
