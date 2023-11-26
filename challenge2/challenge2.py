# challenge2.py

def two_positive(a, b, c):
    # Count the number of positive numbers among a, b, and c
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    # Return True if exactly two of the three numbers are positive
    return positive_count == 2

# Test examples
print(two_positive(2, 4, -3))  # Output: True
print(two_positive(-4, 6, 8))  # Output: True
print(two_positive(4, -6, 9))  # Output: True
print(two_positive(-4, 6, 0))  # Output: False
