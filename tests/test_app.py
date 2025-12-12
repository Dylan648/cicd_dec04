import sys
from pathlib import Path
import pytest
import math

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import (
    add, subtract, multiply, divide,
    square, square_root, logarithm, sine, cosine, percentage
)


class TestBasicOperations:
    
    def test_add_positive_numbers(self):
        assert add(5, 6) == 11
    
    def test_add_negative_numbers(self):
        assert add(-5, -3) == -8
    
    def test_add_mixed_signs(self):
        assert add(10, -5) == 5
    
    def test_add_zero(self):
        assert add(5, 0) == 5
        assert add(0, 0) == 0
    
    def test_add_floats(self):
        assert add(2.5, 3.7) == pytest.approx(6.2)
    
    def test_subtract_positive_numbers(self):
        assert subtract(10, 5) == 5
    
    def test_subtract_negative_numbers(self):
        assert subtract(-5, -3) == -2
    
    def test_subtract_mixed_signs(self):
        assert subtract(5, -3) == 8
    
    def test_subtract_zero(self):
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
    
    def test_subtract_floats(self):
        assert subtract(10.5, 3.2) == pytest.approx(7.3)
    
    def test_multiply_positive_numbers(self):
        assert multiply(4, 5) == 20
    
    def test_multiply_negative_numbers(self):
        assert multiply(-3, -4) == 12
    
    def test_multiply_mixed_signs(self):
        assert multiply(5, -3) == -15
    
    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0
        assert multiply(0, 0) == 0
    
    def test_multiply_floats(self):
        assert multiply(2.5, 4.0) == pytest.approx(10.0)
    
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5
    
    def test_divide_negative_numbers(self):
        assert divide(-10, -2) == 5
    
    def test_divide_mixed_signs(self):
        assert divide(10, -2) == -5
    
    def test_divide_floats(self):
        assert divide(7.5, 2.5) == pytest.approx(3.0)
    
    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
    
    def test_divide_zero_by_number(self):
        assert divide(0, 5) == 0


class TestAdvancedOperations:
    def test_square_positive_number(self):
        assert square(5) == 25
    
    def test_square_negative_number(self):
        assert square(-5) == 25
    
    def test_square_zero(self):
        assert square(0) == 0
    
    def test_square_float(self):
        assert square(2.5) == pytest.approx(6.25)
    
    def test_square_root_positive_number(self):
        assert square_root(25) == 5
    
    def test_square_root_zero(self):
        assert square_root(0) == 0
    
    def test_square_root_float(self):
        assert square_root(6.25) == pytest.approx(2.5)
    
    def test_square_root_negative_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            square_root(-5)

    def test_logarithm_natural_log(self):
        assert logarithm(math.e) == pytest.approx(1.0)
        assert logarithm(1) == pytest.approx(0.0)
    
    def test_logarithm_with_base(self):
        assert logarithm(100, 10) == pytest.approx(2.0)
        assert logarithm(8, 2) == pytest.approx(3.0)
    
    def test_logarithm_zero_or_negative_raises_error(self):
        with pytest.raises(ValueError, match="Logarithm argument must be positive"):
            logarithm(0)
        with pytest.raises(ValueError, match="Logarithm argument must be positive"):
            logarithm(-5)
    
    def test_logarithm_invalid_base_raises_error(self):
        with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
            logarithm(10, 0)
        with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
            logarithm(10, -2)
        with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
            logarithm(10, 1)
    
    def test_sine_zero(self):
        assert sine(0) == pytest.approx(0.0)
    
    def test_sine_pi_over_2(self):
        assert sine(math.pi / 2) == pytest.approx(1.0)
    
    def test_sine_pi(self):
        assert sine(math.pi) == pytest.approx(0.0, abs=1e-10)
    
    def test_sine_negative(self):
        assert sine(-math.pi / 2) == pytest.approx(-1.0)
    
    def test_cosine_zero(self):
        assert cosine(0) == pytest.approx(1.0)
    
    def test_cosine_pi_over_2(self):
        assert cosine(math.pi / 2) == pytest.approx(0.0, abs=1e-10)
    
    def test_cosine_pi(self):
        assert cosine(math.pi) == pytest.approx(-1.0)
    
    def test_cosine_negative(self):
        assert cosine(-math.pi) == pytest.approx(-1.0)
    
    def test_percentage_basic(self):
        assert percentage(50, 200) == 25.0
    
    def test_percentage_whole(self):
        assert percentage(100, 100) == 100.0
    
    def test_percentage_over_hundred(self):
        assert percentage(150, 100) == 150.0
    
    def test_percentage_floats(self):
        assert percentage(3.5, 10.0) == pytest.approx(35.0)
    
    def test_percentage_zero_value(self):
        assert percentage(0, 100) == 0.0
    
    def test_percentage_zero_total_raises_error(self):
        with pytest.raises(ValueError, match="Total cannot be zero for percentage calculation"):
            percentage(50, 0)