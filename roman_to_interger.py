def roman_to_int(s: str) -> int:
    # Roman numeral values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0

  

        # If smaller value before larger value, subtract it
        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total


print(roman_to_int("III"))      # 3
print(roman_to_int("LVIII"))    # 58
print(roman_to_int("MCMXCIV"))  # 1994
