"""
Implementation of RecIntMult algorithm 
given on page 9 of the book Algorithms Illuminated
by Tim Roughgarden

Author: Ibad Desmukh
Date: 2024-09-26

Copyright (c) 2024 Ibad Desmukh. All rights reserved
"""

import math

def count_digits(number):
    """Return the number of digits in the given number"""
    if number == 0:
        return 1
    # log10 provides the power to raise 10 to in order to get the number, and floor rounds it to lowest integer
    return math.floor(math.log10(abs(number))) + 1

def rec_int_mult(x, y):
    """
    Recursively multiply two positive integers using the RecIntMult algorithm
    
    Args:
    x, y: Positive integers to be multiplied
    
    Returns:
    The product of x and y
    """
    
    # Base case: check if the input numbers are single-digit and if so return their product directly
    if x < 10 and y < 10:
        return x * y
    
    # Recursive case
    # Calculate n, the number of digits in x and y
    n_x, n_y = count_digits(x), count_digits(y)

    # Determine n, as maximum of n_x and n_y
    n = max(n_x, n_y)

    # Split x into a and b, y into c and d
    a = x // (10**(n_x//2))
    b = x % (10**(n_x//2))
    c = y // (10**(n_y//2))
    d = y % (10**(n_y//2))

    # Implement recursive multiplication
    ac = rec_int_mult(a, c)
    ad = rec_int_mult(a, d)
    bc = rec_int_mult(b, c)
    bd = rec_int_mult(b, d)

    # Calculate each term of the formula
    term_1 = 10**n * ac
    term_2 = 10**(n // 2) * (ad + bc)
    term_3 = bd

    # Perform basic addition to compute x.y
    return term_1 + term_2 + term_3

# Test the function
print(rec_int_mult(24, 36))