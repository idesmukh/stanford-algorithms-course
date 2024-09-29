"""
Implementation of MergeSort algorithm 
given on pages 16 and 17 of the book Algorithms Illuminated
by Tim Roughgarden

Author: Ibad Desmukh
Date: 2024-09-29

Copyright (c) 2024 Ibad Desmukh. All rights reserved
"""

def merge_sort(A):
	# Base case: check if the array length is 1 or less
	if len(A) <= 1:
		return A

	# Find the middle index of A
	mid_index = len(A) //  2

	# Recursive case: sort the first halve and the second halve
	# Pseudocode: C := recursively sort first half of A
	C = merge_sort(A[:mid_index])
	# Pseudocode: D := recursively sort second half of A
	D = merge_sort(A[mid_index:])

	# Merge the sorted halves
	# Pseudocode: return Merge(C,D)
	return merge(C, D)

def merge(C, D): # Sorted arrays C and D (length n/2 each)
	# Pseudocode: Input: sorted arrays C and D (length n/2 each)
	# Pseudocode: Output: sorted array B (length n)
	n = len(C) + len(D) # Assumption that n is even
	B = [0] * n # Sorted array B (length n)

	# Pseudocode: i := 1
	i = 0 # Index for C
	# Pseudocode: j := 1
	j = 0 # Index for D
	# Pseudocode: for k := 1 to n do
	k = 0 # Index for B

	# Pseudocode: for k := 1 to n do
	while k < n: # While output index is less than the total length of the output array
		# This check is not in the original pseudocode, but necessary for correctness
		if i < len(C) and j < len(D):
			# Pseudocode: if C[i] < D[j] then		
			if C[i] < D[j]:
				# Pseudocode: B[k] := C[i]
				B[k] = C[i] # Populate output array
				# Pseudocode: i := i + 1
				i += 1 # Increment i
			# Pseudocode: else
			else:
				# Pseudocode: B[k] := D[j]
				B[k] = D[j] # Populate output array
				# Pseudocode: j := j + 1
				j += 1 # Increment j
		# These elif and else blocks handle array exhaustion (not in original pseudocode)
		elif i < len(C): # Check if C is exhausted
			B[k] = C[i]
			i += 1
		else: # If C is not exhausted, then D is exhausted
			B[k] = D[j]
			j += 1
		k += 1 # Increment k (implicit in pseudocode's for loop)
	return B

print(merge_sort([4,3,2,3,5]))