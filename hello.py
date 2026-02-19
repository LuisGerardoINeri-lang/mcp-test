#!/usr/bin/env python3
"""
Simple hello world program
"""

def add_numbers(numbers):
    """
    Generic function to add any number of integers from a list
    
    Args:
        numbers: List of integers to sum
    
    Returns:
        Sum of all the integers in the list
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    if not numbers:
        return 0
    return sum(numbers)

print("Hello")
result = add_numbers([5, 10, 15])
print(f"Sum of [5, 10, 15] is: {result}")

# Additional examples
result2 = add_numbers([1, 2, 3, 4, 5])
print(f"Sum of [1, 2, 3, 4, 5] is: {result2}")
