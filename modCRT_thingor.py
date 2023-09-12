'''
Author: hxhBrofessor
Purpose: 
  - To perform modular arithmetic operations (addition, subtraction, multiplication, and exponentiation) on given operands.
  - To display the results in both regular modular notation and their Chinese Remainder Theorem (CRT) representation.
  - To provide a detailed breakdown of each calculation for better understanding.

'''


# Function for modular arithmetic
def mod_arithmetic(a, b, op, mod):
    # Using a dictionary to store the operations
    operations = {
        '+': lambda x, y: (x + y) % mod,
        '-': lambda x, y: (x - y) % mod,
        '*': lambda x, y: (x * y) % mod,
        '^': lambda x, y: pow(x, y, mod)
    }
    if op in operations:
        return operations[op](a, b)
    else:
        raise ValueError("Unsupported operation")

# Function for computing CRT representation
def crt_representation(value, mods):
    residues = [value % m for m in mods]
    return ", ".join(f"{res} mod {m}" for res, m in zip(residues, mods))

def main():
    equations = [
        # Add equations as dictionaries
        {
            'expr': "(a): 4 + 7",
            'mod': 15,
            'operands': [
                {'value': 4, 'mods': [3, 5]},
                {'value': 7, 'mods': [3, 5]}
            ],
            'op': '+'
        },
        {
            'expr': "(b): 8 - (3 * 4)",
            'mod': 15,
            'operands': [
                {'value': 8, 'mods': [3, 5]},
                {'value': 12, 'mods': [3, 5]}
            ],
            'op': '-'
        },
        {
            'expr': "(c): 3^2 + 6",
            'mod': 15,
            'operands': [
                {'value': 9, 'mods': [3, 5]},
                {'value': 6, 'mods': [3, 5]}
            ],
            'op': '+'
        },
        {
            'expr': "(d): 3^2 - 4",
            'mod': 15,
            'operands': [
                {'value': 9, 'mods': [3, 5]},
                {'value': 4, 'mods': [3, 5]}
            ],
            'op': '-'
        }
    ]
    

    for eq in equations:
        # Modular arithmetic result
        result = mod_arithmetic(
            eq['operands'][0]['value'], 
            eq['operands'][1]['value'], 
            eq['op'], 
            eq['mod']
        )

        # Store CRT representations for reusability
        operand1_crt = crt_representation(eq['operands'][0]['value'], eq['operands'][0]['mods'])
        operand2_crt = crt_representation(eq['operands'][1]['value'], eq['operands'][1]['mods'])
        result_crt = crt_representation(result, eq['operands'][0]['mods'])

        # Format the output
        print(f"{eq['expr']} (mod {eq['mod']}) = < {operand1_crt} > {eq['op']} < {operand2_crt} >")
        print(f"Result in CRT representation: < {result_crt} >")
        print(f"Result in mod {eq['mod']}: < {result} mod {eq['mod']} >")
        print("----" * 10)  # Separator line


if __name__ == "__main__":
    main()
