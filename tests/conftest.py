import pytest

from app.calculation import AddCalculation, CalculationFactory, DivideCalculation, MultiplyCalculation, SubtractCalculation

@pytest.fixture(autouse=True)
def setup_calculation_factory():

    CalculationFactory.reset_calculations()

    CalculationFactory.register_calculation('add')(AddCalculation)
    CalculationFactory.register_calculation('divide')(DivideCalculation)
    CalculationFactory.register_calculation('multiply')(MultiplyCalculation)
    CalculationFactory.register_calculation('subtract')(SubtractCalculation)
