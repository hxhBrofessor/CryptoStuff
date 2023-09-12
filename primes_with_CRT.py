'''
Author: hxhBrofessor
Purpose: To find integers that are relatively prime to 
a given number (n) and represent them in the form of Chinese Remainder Theorem (CRT) 
using the prime factors of (n).

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

# Function to find integers relatively prime to n and represent them in CRT
def relatively_prime_and_crt(n):
    # Find prime factors
    factors = find_factors(n)
    
    # Precompute CRT representation string
    crt_str_template = " < " + ", ".join(f"{{}} mod {factor}" for factor in factors) + " >"
    
    # Iterate through numbers and check if they are relatively prime to n
    results = []
    for a in range(1, n):
        if all(a % factor != 0 for factor in factors):
            crt_representation = crt_str_template.format(*(a % factor for factor in factors))
            results.append({
                'integer': a,
                'CRT': crt_representation
            })
    
    return results

# Example: Finding integers relatively prime to 15
n = 15
results = relatively_prime_and_crt(n)
for r in results:
    print(f"{r['integer']} mod {n} becomes {r['CRT']}")
