from abc import ABC, abstractmethod

from app.operation import Operation

class Calculation(ABC):

    def __init__(self, a: float, b: float) -> None:

        # All subclasses should have these same attributes, i.e. the two numbers that are being operated on
        self.a = a
        self.b = b

    @abstractmethod
    def execute(self) -> float:

        # Has to be inherited by each of the subclasses.
        # Performs the actual calculation.
        pass # pragma: no cover

    def __str__(self) -> str:

        # String representation of the object that describes the calculation
        return f'{self.__class__.__name__}: {self.a} {self.__class__.__name__.replace('Calculation', '')} {self.b} = {self.execute()}'

    def __repr__(self) -> str:

        # Return a printout of the object, including its class name and its data
        return f'{self.__class__.__name__}(a={self.a}, b={self.b})'

class CalculationFactory:

    '''
    Allow dynamic creation of different Calculation subclasses, by storing a dictionary (_calculations) that maps operation to class name.
    '''

    _calculations = {}

    @classmethod
    def reset_calculations(cls):

        cls._calculations.clear()

    @classmethod
    def register_calculation(cls, calculation_type: str):

        # Add calculation_type to the dictionary that maps operation to class name

        def decorator(subclass):

            if calculation_type.lower() in cls._calculations:
                raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
            cls._calculations[calculation_type.lower()] = subclass
            return subclass

        return decorator

    @classmethod
    def create_calculation(cls, calculation_type: str, a: float, b: float) -> Calculation:

        # Access _calucations dictionary to instantiate an object of the type corresponding to calculation_type

        calculation_class = cls._calculations.get(calculation_type.lower())
        if not calculation_class:
            valid_types = ', '.join(sorted(list(cls._calculations.keys())))
            raise ValueError(f"Unsupported calculation type: '{calculation_type}'. Available types: {valid_types}")

        return calculation_class(a, b)

'''
Create each Calculation subclass using CalculationFactory based on operation name (ex. add).
Each subclass is the same, except that the execute method calls a different Operation.
'''

@CalculationFactory.register_calculation('add')
class AddCalculation(Calculation):

    def execute(self) -> float:
        return Operation.addition(self.a, self.b)

@CalculationFactory.register_calculation('subtract')
class SubtractCalculation(Calculation):

    def execute(self) -> float:
        return Operation.subtraction(self.a, self.b)

@CalculationFactory.register_calculation('multiply')
class MultiplyCalculation(Calculation):

    def execute(self) -> float:
        return Operation.multiplication(self.a, self.b)

@CalculationFactory.register_calculation('divide')
class DivideCalculation(Calculation):

    def execute(self) -> float:
        # Division by 0 is handled in Operation.division
        return Operation.division(self.a, self.b)
