roman_dict = {"M": 1000,
              "CM": 900,
              "D": 500,
              "CD": 400,
              "C": 100,
              "XC": 90,
              "L": 50,
              "XL": 40,
              "X": 10,
              "IX": 9,
              "V": 5,
              "IV": 4,
              "I": 1}


def int_to_roman(a_int):
    """Given a decimal integer number, convert it to a roman number."""
    roman = ""
    for r in roman_dict.keys():
        r_int = a_int // roman_dict[r]
        a_int %= roman_dict[r]
        roman += r * r_int
    return roman
