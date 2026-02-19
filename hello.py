#!/usr/bin/env python3
"""
Simple hello world program
"""

def add_three_integers(a, b, c):
    """
    Function to add three integers
    
    Args:
        a: First integer
        b: Second integer
        c: Third integer
    
    Returns:
        Sum of the three integers
    """
    return a + b + c

print("Hello")
result = add_three_integers(5, 10, 15)
print(f"Sum of 5, 10, and 15 is: {result}")
