"""
Implementation of Divide and Conquer Merge algorithm 
given in Problem 1.4 on page 34 of the book Algorithms Illuminated
by Tim Roughgarden

Author: Ibad Desmukh
Date: 2024-10-1

Copyright (c) 2024 Ibad Desmukh. All rights reserved
"""

"""
k: number of arrays
n: number of elements in each array
"""

def merge(sorted_arrays, n):
    k = len(sorted_arrays) # k: number of arrays

    # Check if there is more than one array to merge
    if k < 2:
        return sorted_arrays

    # If there is more than one array
    # a) pair up the arrays
    # b) for each pair create a new merged array
    # c) store these new merged arrays in a new list
    else:
        merged_pairs = []
        i = 0

        while i < k:
            if i + 1 < k:
                merged = merge_two_arrays(sorted_arrays[i],sorted_arrays[i + 1])
                merged_pairs.append(merged)
            else:
                merged_pairs.append(sorted_arrays[i])
            i += 2

        return merge(merged_pairs, len(merged_pairs[0]))

def merge_two_arrays(C, D): # Sorted arrays C and D (length n/2 each)
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

print(merge([[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 3, 5]], 4))