# challenge3.py

def solve(word):
    # Calculate the value of consonant substrings
    consonant_values = [ord(c) - ord('a') + 1 for c in word if c not in 'aeiou']
    
    # Return the sum of consonant values
    return sum(consonant_values)

# Test examples
print(solve("zodiacs"))   # Output: 26
print(solve("strength"))  # Output: 57
