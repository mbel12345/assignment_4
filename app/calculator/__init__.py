import sys

from app.calculation import CalculationFactory

class Calculator:

    '''
    This class is a REPL calculator that can perform Addition, Subtraction, Multiplication, and Division.
    It takes inputs from the user in the format <operand> <num_1> <num_2> and shows the user the result of the operation.
    '''

    help_message = '''
Calculator REPL Help
--------------------
Usage:
    <operation> <number1> <number2>
    - Perform a calculation with the specified operation and two numbers.
    - Supported operations:
        add       : Adds two numbers.
        subtract  : Subtracts the second number from the first.
        multiply  : Multiplies two numbers.
        divide    : Divides the first number by the second.

Special Commands:
    help      : Display this help message.
    history   : Show the history of calculations.
    exit      : Exit the calculator.

Examples:
    add 10 5
    subtract 15.5 3.2
    multiply 7 8
    divide 20 4
'''

    def __init__(self) -> None:

        self.history = []

    def run(self) -> None:

        print('Welcome to the Professional Calculator REPL!')
        print("Type 'help' for instructions or 'exit' to quit.\n")

        # Keep prompting the user for calculations until they type 'exit'
        while True:

            try:

                user_input: str = input(">> ").strip()

                if user_input == 'exit':
                    print('Exiting calculator. Goodbye!')
                    sys.exit(0)
                elif user_input == 'help':
                    self.display_help()
                    continue
                elif user_input == 'history':
                    self.display_history()
                    continue

                try:
                    # Extract the parts of the user input (operation and 2 numbers)
                    parts = user_input.split()
                    if len(parts) != 3: # LBYL (look before you leap) error handling, by checking the number of inputs
                        print('Invalid input. Please follow the format: <operation> <num1> <num2>')
                        continue
                    operation = parts[0]
                    num_1 = float(parts[1])
                    num_2 = float(parts[2])
                except ValueError: # EAFP (Easier to Ask Forgiveness than Permission) - Handle any kinds of formatting issues
                    print('Invalid input. Please follow the format: <operation> <num1> <num2>')
                    print("Type 'help' for more information.\n")
                    continue

                # Initialize Calculation and prompt user if operation is invalid
                try:
                    calc = CalculationFactory.create_calculation(operation, num_1, num_2)
                except ValueError as e:
                    print(e)
                    print("Type 'help' to see the list of supported operations.\n")
                    continue

                # Do the operation
                try:
                    calc.execute()
                except ZeroDivisionError:
                    print('Cannot divide by zero.')
                    print('Please enter a non-zero divisor.\n')
                    continue
                except Exception as e:
                    print(f'An error occurred during calculation: {e}')
                    print('Please try again.\n')
                    continue

                # Print the result in a nice format
                result_str: str = f'{calc}'
                print(f'Result: {result_str}\n')

                # Save calculation to the history
                self.history.append(calc)

            except KeyboardInterrupt:

                print('\nKeyboard interrupt detected. Exiting calculator. Goodbye!')
                sys.exit(0)

            except EOFError:

                print('\nEOF detected. Exiting calculator. Goodbye!')
                sys.exit(0)

    def display_help(self) -> None:

        # Display usage instructions for the calculator

        print(Calculator.help_message)

    def display_history(self) -> None:

        # Show the commands that the user has entered

        if len(self.history) > 0:
            print('Calculation History:')
            for i, calc in enumerate(self.history, start=1):
                print(f'{i}. {calc}')
        else:
            print('No calculations performed yet.')
