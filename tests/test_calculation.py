import pytest

from typing import Union
from unittest.mock import patch

from app.calculation import AddCalculation, Calculation, CalculationFactory, DivideCalculation, MultiplyCalculation, SubtractCalculation
from app.operation import Operation

# These tests verify that the CalculationFactory design pattern works properly for all Calculation subclasses.

# 12+ positive test cases for each operation.
# 3x3 = 9 positive basic cases for each non-division function, since each of the two inputs can be either 0, positive, or negative.
# 3 other cases for: positive integer with positive float, positive integer with negative float, negative float with zero.
# For division, there are 8 non-error test cases, with the 4 division-by-0 cases being put into their own test case.

Number = Union[int, float]

# Positive cases for addition

@patch.object(Operation, 'addition')
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
        'add_calculation_positive_integers',
        'add_calculation_positive_integer_and_negative_integer',
        'add_calculation_negative_integer_and_positive_integer',
        'add_calculation_negative_integers',
        'add_calculation_zeros',
        'add_calculation_zero_and_negative_integer',
        'add_calculation_negative_integer_and_zero',
        'add_calculation_zero_and_positive_integer',
        'add_calcalation_positive_integer_and_zero',
        'add_calculation_positive_integer_and_positive_float',
        'add_calculation_positive_integer_and_negative_float',
        'add_calculation_negative_float_and_zero',
    ]
)
def test_add_calculation_positive(mock, a: Number, b: Number, expected: Number):

    mock.return_value = expected
    actual = AddCalculation(a, b).execute()
    mock.assert_called_once_with(a, b)
    assert actual == expected

@pytest.mark.parametrize(
    'a, b, expected',
    [
        (2, 5, 7),
        (0, 0, 0),
    ],
    ids=[
        'add_calculation_to_str_positive_integers',
        'add_calculation_to_str_zeros',
    ]
)
@patch.object(Operation, 'addition')
def test_add_calculation_to_str(mock, a, b, expected):

    mock.return_value = expected
    actual = str(AddCalculation(a, b))
    expected = f'AddCalculation: {a} Add {b} = {expected}'
    assert actual == expected

@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'add_calculation_to_repr_positive_integers',
        'add_calculation_to_repr_zeros',
    ]
)
def test_add_calculation_to_repr(a: Number, b: Number):

    actual = repr(AddCalculation(a, b))
    expected = f'AddCalculation(a={a}, b={b})'
    assert actual == expected

# Negative cases for addition

@patch.object(Operation, 'addition')
@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'add_calculation_fail_positive_integers',
        'add_calculation_fail_zeros',
    ]
)
def test_add_calculation_negative(mock, a: Number, b: Number):

    mock.side_effect = Exception('Addition error')
    with pytest.raises(Exception) as error_info:
        AddCalculation(a, b).execute()
    assert str(error_info.value) == 'Addition error'

# Positive cases for subtraction

@patch.object(Operation, 'subtraction')
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
        'subtract_calculation_positive_integers',
        'subtract_calculation_positive_integer_and_negative_integer',
        'subtract_calculation_negative_integer_and_positive_integer',
        'subtract_calculation_negative_integers',
        'subtract_calculation_zeros',
        'subtract_calculation_zero_and_negative_integer',
        'subtract_calculation_negative_integer_and_zero',
        'subtract_calculation_zero_and_positive_integer',
        'subtract_calculation_positive_integer_and_zero',
        'subtract_calculation_positive_integer_and_positive_float',
        'subtract_calculation_positive_integer_and_negative_float',
        'subtract_calculation_negative_float_and_zero',
    ]
)
def test_subract_calculation_positive(mock, a: Number, b: Number, expected: Number):

    mock.return_value = expected
    actual = SubtractCalculation(a, b).execute()
    mock.assert_called_once_with(a, b)
    assert actual == expected, f'Actual = {actual} does not match expected = {expected}'

@pytest.mark.parametrize(
    'a, b, expected',
    [
        (2, 5, -3),
        (0, 0, 0),
    ],
    ids=[
        'subtract_calculation_to_str_positive_integers',
        'sutbract_calculation_to_str_zeros',
    ]
)
@patch.object(Operation, 'subtraction')
def test_subtract_calculation_to_str(mock, a: Number, b: Number, expected: Number):

    mock.return_value = expected
    actual = str(SubtractCalculation(a, b))
    expected = f'SubtractCalculation: {a} Subtract {b} = {expected}'
    assert actual == expected

@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'subtract_calculation_to_repr_positive_integers',
        'subtract_calculation_to_repr_zeros',
    ]
)
def test_subtract_calculation_to_repr(a: Number, b: Number):

    actual = repr(SubtractCalculation(a, b))
    expected = f'SubtractCalculation(a={a}, b={b})'
    assert actual == expected

# Negative cases for subtraction

@patch.object(Operation, 'subtraction')
@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'subtract_calculation_fail_positive_integers',
        'subtract_calculation_fail_zeros',
    ]
)
def test_subtract_calculation_negative(mock, a: Number, b: Number):

    mock.side_effect = Exception('Subtraction error')
    with pytest.raises(Exception) as error_info:
        SubtractCalculation(a, b).execute()
    assert str(error_info.value) == 'Subtraction error'

# Positive cases for multiplication

@patch.object(Operation, 'multiplication')
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
        'mulitply_calculation_positive_integers',
        'mulitply_calculation_positive_integer_and_negative_integer',
        'mulitply_calculation_negative_integer_and_positive_integer',
        'mulitply_calculation_negative_integers',
        'mulitply_calculation_zeros',
        'mulitply_calculation_zero_and_negative_integer',
        'mulitply_calculation_negative_integer_and_zero',
        'mulitply_calculation_zero_and_positive_integer',
        'mulitply_calculation_positive_integer_and_zero',
        'mulitply_calculation_positive_integer_and_positive_float',
        'mulitply_calculation_positive_integer_and_negative_float',
        'mulitply_calculation_negative_float_and_zero',
    ]
)
def test_multiply_calculation_positive(mock, a: Number, b: Number, expected: Number):

    mock.return_value = expected
    actual = MultiplyCalculation(a, b).execute()
    mock.assert_called_once_with(a, b)
    assert actual == expected, f'Actual = {actual} does not match expected = {expected}'

@pytest.mark.parametrize(
    'a, b, expected',
    [
        (2, 5, 10),
        (0, 0, 0),
    ],
    ids=[
        'multiply_calculation_to_str_positive_integers',
        'multiply_calculation_to_str_zeros',
    ]
)
@patch.object(Operation, 'multiplication')
def test_multiply_calculation_to_str(mock, a: Number, b: Number, expected: Number):

    mock.return_value = expected
    actual = str(MultiplyCalculation(a, b))
    expected = f'MultiplyCalculation: {a} Multiply {b} = {expected}'
    assert actual == expected

@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'multiply_calculation_to_repr_positive_integers',
        'multiply_calculation_to_repr_zeros',
    ]
)
def test_multiply_calculation_to_repr(a: Number, b: Number):

    actual = repr(MultiplyCalculation(a, b))
    expected = f'MultiplyCalculation(a={a}, b={b})'
    assert actual == expected

# Negative cases for multiplication

@patch.object(Operation, 'multiplication')
@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'multiply_calculation_fail_positive_integers',
        'multiply_calculation_fail_zeros',
    ]
)
def test_multiply_calculation_negative(mock, a: Number, b: Number):

    mock.side_effect = Exception('Multiplication error')
    with pytest.raises(Exception) as error_info:
        MultiplyCalculation(a, b).execute()
    assert str(error_info.value) == 'Multiplication error'

# Positive cases for division

@patch.object(Operation, 'division')
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
        'divide_calculation_positive_integers',
        'divide_calculation_positive_integer_and_negative_integer',
        'divide_calculation_negative_integer_and_positive_integer',
        'divide_calculation_negative_integers',
        'divide_calculation_zero_and_negative_integer',
        'divide_calculation_zero_and_positive_integer',
        'divide_calculation_positive_integer_and_positive_float',
        'divide_calculation_positive_integer_and_negative_float',
    ]
)
def test_divide_calculation_positive(mock, a: Number, b: Number, expected: Number):

    mock.return_value = expected
    actual = DivideCalculation(a, b).execute()
    mock.assert_called_once_with(a, b)
    assert actual == expected, f'Actual = {actual} does not match expected = {expected}'

@pytest.mark.parametrize(
    'a, b, expected',
    [
        (2, 5, 0.4),
        (0, 1, 0),
    ],
    ids=[
        'divide_calculation_to_str_positive_integers',
        'divide_calculation_to_str_zero_and_positive_integer',
    ]
)
@patch.object(Operation, 'division')
def test_divide_calculation_to_str(mock, a: Number, b: Number, expected: Number):

    mock.return_value = expected
    actual = str(DivideCalculation(a, b))
    expected = f'DivideCalculation: {a} Divide {b} = {expected}'
    assert actual == expected

@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 1),
    ],
    ids=[
        'divide_calculation_to_repr_positive_integers',
        'divide_calculation_to_repr_zero_and_positive_integer',
    ]
)
def test_divide_calculation_to_repr(a: Number, b: Number):

    actual = repr(DivideCalculation(a, b))
    expected = f'DivideCalculation(a={a}, b={b})'
    assert actual == expected

# Negative cases for division

@patch.object(Operation, 'division')
@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 1),
    ],
    ids=[
        'divide_calculation_fail_positive_integers',
        'divide_calculation_fail_zero_and_positive_integer',
    ]
)
def test_divide_calculation_negative(mock, a: Number, b: Number):

    mock.side_effect = Exception('Division error')
    with pytest.raises(Exception) as error_info:
        DivideCalculation(a, b).execute()
    assert str(error_info.value) == 'Division error'

# Division by 0

@pytest.mark.parametrize(
    'a, b',
    [
        (0, 0),
        (-5, 0),
        (6, 0),
        (-8.7, 0),
    ],
    ids=[
        'divide_zero_and_zero',
        'divide_negative_integer_and_zero',
        'divide_positive_integer_and_zero',
        'divide_negative_float_and_zero',
    ]
)
def test_division_by_zero_error(a: Number, b: Number):

    with pytest.raises(ValueError, match='Division by zero is not allowed.') as division_error:
        DivideCalculation(a, b).execute()

    assert 'Division by zero is not allowed.' in str(division_error.value), f'"Division by zero is not allowed" is expected to be in error message, but error message was "{division_error.value}"'

# Invalid types

@pytest.mark.parametrize('calc_function, a, b', [
    (Operation.addition, '50', 10.0),
    (Operation.subtraction, 50, '10.0'),
    (Operation.multiplication, '40', '30'),
    (Operation.division, 0, '0'),
])
def test_operations_invalid_input(calc_function, a, b):

    with pytest.raises(TypeError):
        calc_function(a, b)

'''
-----------------------------------------------------------------
Test Factory
-----------------------------------------------------------------
'''

# Verify the object types and data are set correctly

@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'factory_create_add_calculation_positive_integers',
        'factory_create_add_calculation_zeros',
    ]
)
def test_factory_create_add_calculation(a: Number, b: Number):

    a = 0
    b = 5.5
    calc = CalculationFactory.create_calculation('add', a, b)
    assert isinstance(calc, AddCalculation)
    assert calc.a == a
    assert calc.b == b

@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'factory_create_subtract_calculation_positive_integers',
        'factory_create_subtract_calculation_zeros',
    ]
)
def test_factory_create_subtract_calculation(a: Number, b: Number):

    a = 0
    b = 5.5
    calc = CalculationFactory.create_calculation('subtract', a, b)
    assert isinstance(calc, SubtractCalculation)
    assert calc.a == a
    assert calc.b == b

@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'factory_create_multiply_calculation_positive_integers',
        'factory_create_multiply_calculation_zeros',
    ]
)
def test_factory_create_multipy_calculation(a: Number, b: Number):

    a = 0
    b = 5.5
    calc = CalculationFactory.create_calculation('multiply', a, b)
    assert isinstance(calc, MultiplyCalculation)
    assert calc.a == a
    assert calc.b == b

@pytest.mark.parametrize(
    'a, b',
    [
        (2, 5),
        (0, 0),
    ],
    ids=[
        'factory_create_divide_calculation_positive_integers',
        'factory_create_divide_calculation_zeros',
    ]
)
def test_factory_create_divide_calculation(a: Number, b: Number):

    a = 0
    b = 5.5
    calc = CalculationFactory.create_calculation('divide', a, b)
    assert isinstance(calc, DivideCalculation)
    assert calc.a == a
    assert calc.b == b

# Test invalid calculation type
@pytest.mark.parametrize(
    'calc_type',
    [
        ('long_divide'),
        ('long_multiply'),
    ],
    ids=[
        'invalid_calculation_long_divide',
        'invalid_calculation_long_multiply',
    ]
)
def test_factory_create_invalid_calculation_type(calc_type):

    a = 0
    b = 5.5
    with pytest.raises(ValueError) as error_info:
        CalculationFactory.create_calculation(calc_type, a, b)
    assert f"Unsupported calculation type: '{calc_type}'" in str(error_info.value)

# Test attempting to register the same operation twice
@pytest.mark.parametrize(
    'operation',
    [
        ('add'),
        ('subtract'),
    ],
    ids=[
        'add_calculation_duplicate_registration',
        'subtract_calculation_duplicate_registration',
    ]
)
def test_factory_duplicate_registration(operation):

    with pytest.raises(ValueError) as error_info:

        @CalculationFactory.register_calculation(operation) # Already added as a pytest fixture in conftest.py
        class DummyCalculation(Calculation):

            def execute(self) -> float:
                return Operation.addition(self.a, self.b)

        assert f"Calculation type '{operation}' is already registered." in str(error_info.value)
