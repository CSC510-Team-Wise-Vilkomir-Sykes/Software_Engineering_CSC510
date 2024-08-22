import pytest
from number_translator import int_to_roman 

def test_failure():
    assert int_to_roman(2024) == "MMXX" 

def test_failure2():
    assert int_to_roman(57) == "LVI"

def test_failure3():
    assert int_to_roman(9) == "X"

def test_pass():
    assert int_to_roman(1994) == "MCMXCIV"

def test_pass2():
    assert int_to_roman(58) == "LVIII"

def test_pass3():
    assert int_to_roman(10) == "X"
