# Version 3.6

def merge(left, right):
	"""
	Merge Routine:
	Merges two given arrays into a single sorted array by comparing 
	individual values from both arrays.
	Input : left and right arrays split by recursive splitting done in mSort.
	Output : single sorted array.
	"""
	i = 0
	j = 0
	result = []

	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		elif right[j] < left[i]:
			result.append(right[j])
			j += 1

	result += left[i:] + right[j:]

	return result

def mSort(arr):
	"""
	Recursively splits the given array into left and right array of equal size
	and calls the merge routine on these split arrays.
	Input : unsorted array
	Output : sorted array
	"""

	# Base case when length of array is 1
	if len(arr) == 1:
		return arr
	
	mid = int(len(arr)//2)
	# Recursive splitting of main array into left and right children
	left = mSort(arr[:mid])
	right = mSort(arr[mid:])
	# Calling the merge routine on the split arrays
	return merge(left, right)
