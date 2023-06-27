import z3

print("""
==================================
SMT Solver
Instructions:
    1. Enter your variables
    2. Enter your constraints
    3. Press Ctrl-C when you are done with entering all the constraints
==================================
      """)

variable_input = input("Enter variables split by spaces: ")
variable_input = variable_input.split(' ')
variables = {}
for var in variable_input:
    variables[var] = z3.Int(var)

solver = z3.Solver()
while True:
    try:
        constraint = input("Enter the constraint: ")
        processed_constraint = ""
        for char in constraint:
            if char in variables:
                processed_constraint += f"variables['{char}']"
            else:
                processed_constraint += char
        try:
            solver.add(eval(processed_constraint))
        except SyntaxError as e:
            print(f"Invalid Syntax! {e}")
        except NameError:
            print("Name does not exist!")
        except z3.z3types.Z3Exception:
            print("Invalid!")
    except KeyboardInterrupt:
        if solver.check() == z3.sat: # check if satisfiable
            print("\nSOLUTION")
            print(solver.model())
        else:
            print("\nNO SOLUTION")
        break
