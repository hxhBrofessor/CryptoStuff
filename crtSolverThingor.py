'''
Author: hxhBrofessor

Purpose: Purpose: To solve systems of simultaneous linear congruences using the
Chinese Remainder Theorem and the Extended Euclidean Algorithm.


'''

from math import gcd
from functools import reduce
from itertools import combinations

# Function to find the multiplicative inverse using Extended Euclidean Algorithm
def mod_inv(a, m):
    d, x, y = extended_gcd(a, m)
    if d != 1:
        return None  # multiplicative inverse doesn't exist
    else:
        return x % m

# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = extended_gcd(b, a % b)
    return d, y, x - (a // b) * y

# Function to check if all numbers in a list are pairwise coprime
def are_coprime(numbers):
    for m1, m2 in combinations(numbers, 2):
        if gcd(m1, m2) != 1:
            return False
    return True

# Function to solve a system of n congruences
def solve_congruences(a_values, m_values):
    if not are_coprime(m_values):
        return None, "The moduli are not pairwise coprime; cannot solve the system."
    
    M = reduce(lambda x, y: x * y, m_values)
    x = 0

    for a, m in zip(a_values, m_values):
        M_i = M // m
        M_i_inv = mod_inv(M_i, m)
        if M_i_inv is None:
            return None, "Multiplicative inverse doesn't exist; cannot solve."
        x += a * M_i * M_i_inv

    x %= M
    
    return x, M

# List of equations to solve
equation_sets = [
    {'a_values': [3, 4], 'm_values': [7, 9]},
    {'a_values': [137, 87], 'm_values': [423, 191]},
    {'a_values': [133, 237], 'm_values': [451, 697]},
    {'a_values': [5, 6, 7], 'm_values': [9, 10, 11]},
    {'a_values': [37, 22, 18], 'm_values': [43, 49, 71]}
]

# Solve each set of equations
for i, equation_set in enumerate(equation_sets, 1):
    solution, M = solve_congruences(equation_set['a_values'], equation_set['m_values'])
    if solution is not None:
        print(f"Solution to equation set {i}: is {solution}")
    else:
        print(f"Equation set {i}: {M}")
