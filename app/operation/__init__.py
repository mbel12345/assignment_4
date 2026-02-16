class Operation:

    @staticmethod
    def addition(a: float, b: float) -> float:

        # Add a and b
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:

        # Subtract a and b
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:

        # Multiply a and b
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:

        # Divide a by b. Raise an error if b is zero.
        if b == 0:
            raise ZeroDivisionError('Division by zero is not allowed.')

        return a / b
