import pytest
from number_translator import int_to_roman 

def test_pass():
    assert int_to_roman(1994) == "MCMXCIV"
    # assert int_to_roman(58) == "LVIII"
    # assert int_to_roman(10) == "X"

def test_failure():
    assert int_to_roman(2024) == "MMXX" 
    # assert int_to_roman(57) == "LVI"
    # assert int_to_roman(9) == "X"
