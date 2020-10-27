import re

roman_dict = {"I": 1,
              "IV": 4,
              "V": 5,
              "IX": 9,
              "X": 10,
              "XL": 40,
              "L": 50,
              "XC": 90,
              "C": 100,
              "CD": 400,
              "D": 500,
              "CM": 900,
              "M": 1000}


def roman_to_int(a_roman):
    """Given a roman number, convert it to a decimal integer."""
    roman_list = re.findall(r"CM|CD|XC|XL|IX|IV|M|D|C|X|V|L|I", a_roman)
    a_int = 0
    for r in roman_list:
        a_int += roman_dict[r]
    return a_int
