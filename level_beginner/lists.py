"""
List Theory
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# From 3 to 6 (7-1)
print(numbers[3:7])

# Odd numbers (1 to 10, step 2)
print(numbers[1::2])

# Even numbers (0 to 10, step 2)
print(numbers[0::2])
print(numbers[::2])

# From 0 to 2 (3-1)
print(numbers[0:3])
print(numbers[:3])

# From 3 to all
print(numbers[3:])

# Last 3 numbers
print(numbers[-3:])
