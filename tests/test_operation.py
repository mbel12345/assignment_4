import pytest

from typing import Union
from unittest.mock import patch

from app.operation import Operation

# These tests verify the math itself in the operations.

# 12 total test cases for each operation.
# 3x3 = 9 cases for each non-division function, since each of the two inputs can be either 0, positive, or negative.
# 3 other cases for: positive integer with positive float, positive integer with negative float, negative float with zero.
# For division, there are 8 non-error test cases, with the 4 division-by-0 cases being put into their own test case.

Number = Union[int, float]

# Positive cases for addition
@pytest.mark.parametrize(
    'a, b, expected',
    [
        (2, 5, 7),
        (1, -4, -3),
        (-5, 10, 5),
        (-3, -4, -7),
        (0, 0, 0),
        (0, -4, -4),
        (-5, 0, -5),
        (0, 4, 4),
        (6, 0, 6),
        (4, 0.5, 4.5),
        (4, -0.5, 3.5),
        (-8.7, 0, -8.7),
    ],
    ids=[
        'add_operation_positive_integers',
        'add_operation_positive_integer_and_negative_integer',
        'add_operation_negative_integer_and_positive_integer',
        'add_operation_negative_integers',
        'add_operation_zeros',
        'add_operation_zero_and_negative_integer',
        'add_operation_negative_integer_and_zero',
        'add_operation_zero_and_positive_integer',
        'add_operation_positive_integer_and_zero',
        'add_operation_positive_integer_and_positive_float',
        'add_operation_positive_integer_and_negative_float',
        'add_operation_negative_float_and_zero',
    ]
)
def test_addition(a: Number, b: Number, expected: Number):

    actual = Operation.addition(a, b)
    assert actual == expected, f'Actual = {actual} does not match expected = {expected}'

# Negative cases for addition
@patch.object(Operation, 'addition')
@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'add_operation_fail_positive_integers',
        'add_operation_fail_zeros',
    ]
)
def test_add_operation_negative(mock, a: Number, b: Number):

    mock.side_effect = Exception('Addition error')
    with pytest.raises(Exception) as error_info:
        Operation.addition(a, b)
    assert str(error_info.value) == 'Addition error'

# Positive cases for subtraction
@pytest.mark.parametrize(
    'a, b, expected',
    [
        (2, 5, -3),
        (1, -4, 5),
        (-5, 10, -15),
        (-3, -4, 1),
        (0, 0, 0),
        (0, -4, 4),
        (-5, 0, -5),
        (0, 4, -4),
        (6, 0, 6),
        (4, 0.5, 3.5),
        (4, -0.5, 4.5),
        (-8.7, 0, -8.7),
    ],
    ids=[
        'subtract_operation_positive_integers',
        'subtract_operation_positive_integer_and_negative_integer',
        'subtract_operation_negative_integer_and_positive_integer',
        'subtract_operation_negative_integers',
        'subtract_operation_zeros',
        'subtract_operation_zero_and_negative_integer',
        'subtract_operation_negative_integer_and_zero',
        'subtract_operation_zero_and_positive_integer',
        'subtract_operation_positive_integer_and_zero',
        'subtract_operation_positive_integer_and_positive_float',
        'subtract_operation_positive_integer_and_negative_float',
        'subtract_operation_negative_float_and_zero',
    ]
)
def test_subtraction(a: Number, b: Number, expected: Number):

    actual = Operation.subtraction(a, b)
    assert actual == expected, f'Actual = {actual} does not match expected = {expected}'

# Negative cases for subtraction
@patch.object(Operation, 'subtraction')
@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'subtract_operation_fail_positive_integers',
        'subtract_operation_fail_zeros',
    ]
)
def test_subtract_operation_negative(mock, a: Number, b: Number):

    mock.side_effect = Exception('Subtraction error')
    with pytest.raises(Exception) as error_info:
        Operation.subtraction(a, b)
    assert str(error_info.value) == 'Subtraction error'

# Positive cases for multiplication
@pytest.mark.parametrize(
    'a, b, expected',
    [
        (2, 5, 10),
        (1, -4, -4),
        (-5, 10, -50),
        (-3, -4, 12),
        (0, 0, 0),
        (0, -4, 0),
        (-5, 0, 0),
        (0, 4, 0),
        (6, 0, 0),
        (4, 0.5, 2),
        (4, -0.5, -2),
        (-8.7, 0, 0),
    ],
    ids=[
        'multiply_operation_positive_integers',
        'multiply_operation_positive_integer_and_negative_integer',
        'multiply_operation_negative_integer_and_positive_integer',
        'multiply_operation_negative_integers',
        'multiply_operation_zeros',
        'multiply_operation_zero_and_negative_integer',
        'multiply_operation_negative_integer_and_zero',
        'multiply_operation_zero_and_positive_integer',
        'multiply_operation_positive_integer_and_zero',
        'multiply_operation_positive_integer_and_positive_float',
        'multiply_operation_positive_integer_and_negative_float',
        'multiply_operation_negative_float_and_zero',
    ]
)
def test_multiplication(a: Number, b: Number, expected: Number):

    actual = Operation.multiplication(a, b)
    assert actual == expected, f'Actual = {actual} does not match expected = {expected}'

# Negative cases for multiplication
@patch.object(Operation, 'multiplication')
@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'multiply_operation_fail_positive_integers',
        'multiply_operation_fail_zeros',
    ]
)
def test_multiply_operation_negative(mock, a: Number, b: Number):

    mock.side_effect = Exception('Multiplication error')
    with pytest.raises(Exception) as error_info:
        Operation.multiplication(a, b)
    assert str(error_info.value) == 'Multiplication error'

# Positive cases for division
@pytest.mark.parametrize(
    'a, b, expected',
    [
        (2, 5, 0.4),
        (1, -4, -0.25),
        (-5, 10, -0.5),
        (-3, -4, 0.75),
        (0, -4, 0),
        (0, 4, 0),
        (4, 0.5, 8),
        (4, -0.5, -8),
    ],
    ids=[
        'divide_operation_positive_integers',
        'divide_operation_positive_integer_and_negative_integer',
        'divide_operation_negative_integer_and_positive_integer',
        'divide_operation_negative_integers',
        'divide_operation_zero_and_negative_integer',
        'divide_operation_zero_and_positive_integer',
        'divide_operation_positive_integer_and_positive_float',
        'divide_operation_positive_integer_and_negative_float',
    ]
)
def test_division_success(a: Number, b: Number, expected: Number):

    actual = Operation.division(a, b)
    assert actual == expected, f'Actual = {actual} does not match expected = {expected}'

# Negative cases for division
@patch.object(Operation, 'division')
@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'division_operation_fail_positive_integers',
        'division_operation_fail_zeros',
    ]
)
def test_divide_operation_negative(mock, a: Number, b: Number):

    mock.side_effect = Exception('Division error')
    with pytest.raises(Exception) as error_info:
        Operation.division(a, b)
    assert str(error_info.value) == 'Division error'

# division by 0
@pytest.mark.parametrize(
    'a, b',
    [
        (0, 0),
        (-5, 0),
        (6, 0),
        (-8.7, 0),
    ],
    ids=[
        'divide_operation_zero_and_zero',
        'divide_operation_negative_integer_and_zero',
        'divide_operation_positive_integer_and_zero',
        'divide_operation_negative_float_and_zero',
    ]
)
def test_vision_by_zero_error(a: Number, b: Number):

    with pytest.raises(ValueError, match='Division by zero is not allowed.') as division_error:
        Operation.division(a, b)

    assert 'Division by zero is not allowed.' in str(division_error.value), f'"Division by zero is not allowed" is expected to be in error message, but error message was "{division_error.value}"'

@pytest.mark.parametrize('calc_function, a, b', [
    (Operation.addition, '50', 10.0),
    (Operation.subtraction, 50, '10.0'),
    (Operation.multiplication, '40', '30'),
    (Operation.division, 0, '0'),
])
def test_operation_invalid_input(calc_function, a, b):

    with pytest.raises(TypeError):
        calc_function(a, b)
