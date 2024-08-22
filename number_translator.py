def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.
    
    Parameters:
    num (int): The integer to convert.
    
    Returns:
    str: The Roman numeral representation of the integer.
    """
    mapping = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    roman_numeral = ''
    # Convert the integer to a Roman numeral
    for (value, symbol) in mapping:
        while num >= value:
            roman_numeral += symbol
            num -= value
    return roman_numeral

try:
    arabic_number = int(input("Enter an integer to convert to Roman numerals: "))
    if arabic_number <= 0:
        raise ValueError("Number must be greater than 0")
    print(f"The Roman numeral for {arabic_number} is {int_to_roman(arabic_number)}")
except ValueError as e:
    print(f"Invalid input: {e}")


# Example inputs and outputs:
# Input: 1994 Output: MCMXCIV
# Input: 58 Output: LVIII   
# Input:9 Output: IX