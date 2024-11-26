import pytest
from app.calculator import Calculator

class TestCalc:
    def setup_method(self):
        self.calculator = Calculator()

    def test_add(self):
        assert self.calculator.add(1, 2) == 3
        assert self.calculator.add(-1, 1) == 0
        assert self.calculator.add(0, 0) == 0

    def test_subtract(self):
        assert self.calculator.subtract(5, 3) == 2
        assert self.calculator.subtract(-1, -1) == 0
        assert self.calculator.subtract(0, 1) == -1

    def test_multiply(self):
        assert self.calculator.multiply(3, 5) == 15
        assert self.calculator.multiply(-1, 1) == -1
        assert self.calculator.multiply(0, 123) == 0

    def test_divide(self):
        assert self.calculator.divide(10, 2) == 5
        assert self.calculator.divide(-6, -2) == 3
        assert self.calculator.divide(0, 1) == 0
        with pytest.raises(ValueError):
            self.calculator.divide(10, 0)
