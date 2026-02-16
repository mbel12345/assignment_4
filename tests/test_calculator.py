import pytest
import sys

from io import StringIO
from unittest.mock import patch

from app.calculation import AddCalculation
from app.calculator import Calculator

# This tests that the Calculator that the user sees works end-to-end

# Full testing of the operations is covered in test_operations.py.
# So, the parametrized testing here (test_calculator.py) is not intended to cover all cases, but rather demonstrate parametrized testing as a concept.
# Testing in here (test_calculator.py) is primarily for testing the REPL structure and user interactions.

def run_calc(monkeypatch, capsys, user_inputs):

    # Simulate reading input from user, and return the output from the calculator app.

    inputs = iter(user_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    for user_input in user_inputs:
        monkeypatch.setattr(sys, 'stdin', StringIO(user_input))

    calc = Calculator()
    with pytest.raises(SystemExit) as error_info:
        calc.run()

    captured = capsys.readouterr().out
    return captured

def check_result(actual, expected):

    # Check that the calculator gives a welcome message, an answer/error (expected) for user's question, and an exit message.

    actual = actual.strip()
    expected = f'''
Welcome to the Professional Calculator REPL!
Type 'help' for instructions or 'exit' to quit.
{'\n' + expected if expected else ''}
Exiting calculator. Goodbye!
'''.strip()
    assert actual == expected

'''
----------------------------------------------------------------
Tests for valid inputs
----------------------------------------------------------------
'''

# addition
@pytest.mark.parametrize(
    'inputs, expected',
    [
        (['add 10 5', 'exit'], 'AddCalculation: 10.0 Add 5.0 = 15.0\n'),
        (['add -1 2.5', 'exit'], 'AddCalculation: -1.0 Add 2.5 = 1.5\n'),
    ],
    ids=[
        'add_calculator_positive_integer_and_positive_integer',
        'add_calculator_negative_integer_and_positive_float',
    ]
)
def test_addition(monkeypatch, capsys, inputs, expected):

    # Test addition for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, f'Result: {expected}')

# subtraction
@pytest.mark.parametrize(
    'inputs, expected',
    [
        (['subtract 10 5', 'exit'], 'SubtractCalculation: 10.0 Subtract 5.0 = 5.0\n'),
        (['subtract -1 2.5', 'exit'], 'SubtractCalculation: -1.0 Subtract 2.5 = -3.5\n'),
    ],
    ids=[
        'subtract_calculator_positive_integer_and_positive_integer',
        'subtract_calculator_negative_integer_and_positive_float',
    ]
)
def test_subtraction(monkeypatch, capsys, inputs, expected):

    # Test subtraction for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, f'Result: {expected}')

# multiplication
@pytest.mark.parametrize(
    'inputs, expected',
    [
        (['multiply 10 5', 'exit'], 'MultiplyCalculation: 10.0 Multiply 5.0 = 50.0\n'),
        (['multiply -1 2.5', 'exit'], 'MultiplyCalculation: -1.0 Multiply 2.5 = -2.5\n'),
    ],
    ids=[
        'multiply_calculator_positive_integer_and_positive_integer',
        'multiply_calculator_negative_integer_and_positive_float',
    ]
)
def test_multiplication(monkeypatch, capsys, inputs, expected):

    # Test multiplication for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, f'Result: {expected}')

# division
@pytest.mark.parametrize(
    'inputs, expected',
    [
        (['divide 10 5', 'exit'], 'DivideCalculation: 10.0 Divide 5.0 = 2.0\n'),
        (['divide -1 2.5', 'exit'], 'DivideCalculation: -1.0 Divide 2.5 = -0.4\n'),
    ],
    ids=[
        'divide_calculator_positive_integer_and_positive_integer',
        'divide_calculator_negative_integer_and_positive_float',
    ]
)
def test_division(monkeypatch, capsys, inputs, expected):

    # Test division for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, f'Result: {expected}')

'''
----------------------------------------------------------------
Test error handling
----------------------------------------------------------------
'''

# invalid operation
@pytest.mark.parametrize(
    'inputs',
    [
        (['longdivide 9 3', 'exit']),
        (['min 4 5', 'exit']),
    ],
    ids=[
        'unknown_calculator_operation_longdivice',
        'unknown_calculator_operation_min',
    ]
)
def test_invalid_operation(monkeypatch, capsys, inputs):

    # Test invalid operation for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    assert f"Unsupported calculation type: '{inputs[0].split()[0]}'. Available types: " in actual
    assert f"Type 'help' to see the list of supported operations." in actual

# wrong number of inputs
@pytest.mark.parametrize(
    'inputs',
    [
        (['add 3 4 extra-arg', 'exit']),
        (['add 4 56 5 1_extra extra-arg', 'exit']),
        (['add', 'exit']),
    ],
    ids=[
        'calculator_too_many_inputs_1_extra',
        'calculator_too_many_inputs_2_extra',
        'calculator_too_few_inputs_1_input',
    ]
)
def test_wrong_number_of_inputs(monkeypatch, capsys, inputs):

    # Test sending too may inputs to the REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, 'Invalid input. Please follow the format: <operation> <num1> <num2>')

# invalid input format
@pytest.mark.parametrize(
    'inputs',
    [
        (['add two 7', 'exit']),
        (['add 4 4x', 'exit']),
    ],
    ids=[
        'calculator_invalid_format_number_spelled_out',
        'calculator_invalid_format_invalid_number',
    ]
)
def test_invalid_input_format(monkeypatch, capsys, inputs):

    # Test invalid format for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, "Invalid input. Please follow the format: <operation> <num1> <num2>\nType 'help' for more information.\n")

# division by 0
@pytest.mark.parametrize(
    'inputs',
    [
        (['divide 8 0', 'exit']),
        (['divide -5.5 0', 'exit']),
    ],
    ids=[
        'divide_calculator_positive_integer_and_zero',
        'divide_calculator_negative_float_and_zero',
    ]
)
def test_division_by_zero(monkeypatch, capsys, inputs):

    # Test division by 0 for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, 'Cannot divide by zero.\nPlease enter a non-zero divisor.\n')

@patch.object(AddCalculation, 'execute')
def test_unexpected_error(mock, monkeypatch, capsys):

    # Force the code to go to the try-catch block that handles unexpected errors

    mock.side_effect = Exception('Unknown calculator error.')
    actual = run_calc(monkeypatch, capsys, ['add 3 4', 'exit'])
    check_result(actual, 'An error occurred during calculation: Unknown calculator error.\nPlease try again.\n')

'''
----------------------------------------------------------------
Help
----------------------------------------------------------------
'''

def test_display_help(monkeypatch, capsys):

   # Verify that the help message is as expected

    actual = run_calc(monkeypatch, capsys, ['help', 'exit'])
    expected = '''
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

    check_result(actual, expected)

'''
----------------------------------------------------------------
History
----------------------------------------------------------------
'''
def test_display_history_empty(monkeypatch, capsys):

    actual = run_calc(monkeypatch, capsys, ['history', 'exit'])
    expected = 'No calculations performed yet.'
    check_result(actual, expected)

@pytest.mark.parametrize(
    'inputs, expected',
    [
        (
            ['divide 5 2', 'history', 'exit'],
            '''
Result: DivideCalculation: 5.0 Divide 2.0 = 2.5

Calculation History:
1. DivideCalculation: 5.0 Divide 2.0 = 2.5
            '''.strip()
        ),
        (
            ['add 3 4', 'subtract 3 2', 'multiply 4 5', 'divide 8 2', 'history', 'exit'],
            '''
Result: AddCalculation: 3.0 Add 4.0 = 7.0

Result: SubtractCalculation: 3.0 Subtract 2.0 = 1.0

Result: MultiplyCalculation: 4.0 Multiply 5.0 = 20.0

Result: DivideCalculation: 8.0 Divide 2.0 = 4.0

Calculation History:
1. AddCalculation: 3.0 Add 4.0 = 7.0
2. SubtractCalculation: 3.0 Subtract 2.0 = 1.0
3. MultiplyCalculation: 4.0 Multiply 5.0 = 20.0
4. DivideCalculation: 8.0 Divide 2.0 = 4.0
'''.strip()
        ),
    ],
    ids=[
        'history_with_one_operation',
        'history_with_all_operations',
    ]
)
def test_display_history_with_entries(monkeypatch, capsys, inputs, expected):

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, expected)

'''
----------------------------------------------------------------
Exit
----------------------------------------------------------------
'''

def test_exit(monkeypatch, capsys):

    # Test if user can exit the calculator by running exit immediately
    user_inputs = ['exit']
    inputs = iter(user_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    for user_input in user_inputs:
        monkeypatch.setattr(sys, 'stdin', StringIO(user_input))

    with pytest.raises(SystemExit) as error_info:
        Calculator().run()

    assert error_info.type == SystemExit
    assert error_info.value.code == 0

    actual = capsys.readouterr().out
    check_result(actual, '')

def test_keyboard_interrupt(monkeypatch, capsys):

    # Test that the calculator handles Keyboard Interrupt (Ctrl+C)

    monkeypatch.setattr('builtins.input', lambda *args, **kwargs: (_ for _ in ()).throw(KeyboardInterrupt()))

    calc = Calculator()
    with pytest.raises(SystemExit) as error_info:
        calc.run()

    out = capsys.readouterr().out
    assert 'Keyboard interrupt detected. Exiting calculator. Goodbye!' in out
    assert error_info.value.code == 0

def test_eof_error(monkeypatch, capsys):

    # Test that the calculator handles EOF (Ctrl+D)

    monkeypatch.setattr('builtins.input', lambda *args, **kwargs: (_ for _ in ()).throw(EOFError()))

    calc = Calculator()
    with pytest.raises(SystemExit) as error_info:
        calc.run()

    out = capsys.readouterr().out
    assert 'EOF detected. Exiting calculator. Goodbye!' in out
    assert error_info.value.code == 0
