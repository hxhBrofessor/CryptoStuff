'''
Author: hxhBrofessor
Purpose: To evaluate various modular arithmetic expressions
including addition, subtraction, and finding multiplicative inverses, all under a given modulus.

'''

# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = extended_gcd(b, a % b)
    return d, y, x - (a // b) * y

# Function to find the multiplicative inverse using Extended Euclidean Algorithm
def mod_inv(a, m):
    d, x, y = extended_gcd(a, m)
    if d != 1:
        return None  # multiplicative inverse doesn't exist
    else:
        return x % m

# Main function
def main():
    equations = [
        # Add equations as dictionaries
        {
            'expr': "4 + 7",
            'mod': 15,
            'operands': [4, 7],
            'op': '+'
        },
        {
            'expr': "8 - (3 * 4)",
            'mod': 15,
            'operands': [8, 12],
            'op': '-'
        },
        {
            #modular inverse, only one operand is needed
            'expr': "7^(-1)",
            'mod': 15,
            'operands': [7],
            'op': '^'
        },
        {
            'expr': "3^2 + (6 * 7)",
            'mod': 15,
            'operands': [9, 42],
            'op': '+'
        },
        {
            'expr': "3^2 - 4",
            'mod': 15,
            'operands': [9, 4],
            'op': '-'
        }
    ]

    for eq in equations:
        # Modular arithmetic result
        try:
            if eq['op'] == '^':
                result = mod_inv(eq['operands'][0], eq['mod'])
            elif eq['op'] == '+':
                result = (eq['operands'][0] + eq['operands'][1]) % eq['mod']
            elif eq['op'] == '-':
                result = (eq['operands'][0] - eq['operands'][1]) % eq['mod']

            print(f"Result of {eq['expr']} (mod {eq['mod']}) is: {result}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
