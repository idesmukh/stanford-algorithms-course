"""
Implementation of Sequential Merge algorithm 
given in Problem 1.3 on page 33 of the book Algorithms Illuminated
by Tim Roughgarden

Author: Ibad Desmukh
Date: 2024-09-30

Copyright (c) 2024 Ibad Desmukh. All rights reserved
"""

"""
k: number of arrays
n: number of elements in each array
"""

def merge(A, B):
	# Total length of both arrays, or the length of result array
	n = len(A) + len(B)

	# Initialise empty result array
	result = [0] * n

	i = 0 # Index to keep track of A
	j = 0 # Index to keep track of B
	k = 0 # Index to keep track of result

	# While both A and B have not been exhausted
	while i < len(A) and j < len(B):
		# Add elements based on comparison
		if A[i] < B[j]:
			result[k] = A[i]
			i += 1
		else:
			result[k] = B[j]
			j += 1
		# Increment k to run the while loop
		k += 1

	# If i/j are still less than the lengths of A/B, keep running to add remaining elements to result
	while i < len(A):
		result[k] = A[i]
		i += 1
		k += 1

	while j < len(B):
		result[k] = B[j]
		j += 1
		k += 1

	return result

# Function to recursively run the merge function across arrays
def sequential_merge(arrays):
	result = arrays[0]
	for i in range(1, len(arrays)):
		result = merge(result, arrays[i])
	return result

arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [0, 10, 11]]
print(sequential_merge(arrays))