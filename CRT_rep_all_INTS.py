'''
Author: hxhBrofessor

Purpose: This script calculates the Chinese Remainder Theorem (CRT) representation for all integers 
from 0 to a given number (n-1). 
The CRT representation is constructed using the prime factors of n.
'''

from math import gcd
from functools import reduce

# Function to find factors of a number
def find_factors(n):
    factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)
            while n % i == 0:
                n = n // i
    if n > 1:
        factors.add(n)
    return factors

# Function to find integers and represent them in CRT
def all_numbers_and_crt(n):
    # Find prime factors
    factors = find_factors(n)
    
    # Precompute CRT representation string
    crt_str_template = " < " + ", ".join(f"{{}} mod {factor}" for factor in factors) + " >"
    
    # Iterate through all numbers from 0 to n-1
    results = []
    for a in range(n):
        crt_representation = crt_str_template.format(*(a % factor for factor in factors))
        results.append({
            'integer': a,
            'CRT': crt_representation
        })
    
    return results

# Example: Finding integers relatively prime to 15
n = 15
results = all_numbers_and_crt(n)
for r in results:
    print(f"{r['integer']} mod {n} becomes {r['CRT']}")
