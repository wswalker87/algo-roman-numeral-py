# 1. Write a method TO_ROMAN, TO_ROMAN takes in INPUT_NUMBER (an arabic number)
# 2. Create a OUTPUT string, set to ''
# 3. Create a ROMAN_NUMERAL_TO_ARABIC_MAP that includes roman numerals as keys, arabic numbers as values
# 4. Iterate over ROMAN_NUMERAL_TO_ARABIC_MAP, keep track of ROMAN_NUMERAL and ARABIC_NUMBER
# 5. Set EVENLY_DIVISIBLE_TIMES = INPUT_NUMBER / ARABIC_NUMBER:
# 6. If EVENLY_DIVISIBLE_TIMES >= 1
  # 6a. Append ROMAN_NUMERAL to OUTPUT EVENLY_DIVISIBLE_TIMES
  # 6b. Subtract ARABIC_NUMBER from INPUT_NUMBER EVENLY_DIVISIBLE_TIMES
# 7. Return OUTPUT

def to_roman(num):
    # output = []
    output = ""

    roman_numeral_to_arabic = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
  }

    for k, v in reversed(roman_numeral_to_arabic.items()):
    # for k, v in roman_numeral_to_arabic.items():
        evenly_divisable_times = num // v
        # print(evenly_divisable_times)
        if evenly_divisable_times >= 1:
            output += k * evenly_divisable_times
            num -= (v * evenly_divisable_times)
            # print(output)
        
    return output


# print(to_roman(20)) ## XX
print(to_roman(944)) ## CMXLIV'
# print(to_roman(1)) ## I
# print(to_roman(3)) ## III
# print(to_roman(4)) ## IV
