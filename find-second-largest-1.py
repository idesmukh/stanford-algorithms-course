# Initial implementation of Find Second Largest algorithm
def find_second_largest(input_array):
    n = len(input_array)

    if n == 0:
        return None

    if n == 1:
        return input_array

    if n % 2 > 0:
        return "Input array length is not even"

    largest = input_array[0]
    second_largest = 0

    for i in range(1, n):
        if input_array[i] > largest:
            second_largest = largest
            largest = input_array[i]
    
    return second_largest

print(find_second_largest([2,5,1,9]))