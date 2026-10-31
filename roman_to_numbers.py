def roman_to_integer(s):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0

    for i in range(len(s)):
        current_value = values[s[i]]

        if i + 1 < len(s) and current_value < values[s[i + 1]]:
            total -= current_value
            print(f"{s[i]} is before a larger symbol: subtract {current_value}. Total = {total}")
        else:
            total += current_value
            print(f"Add {current_value} for {s[i]}. Total = {total}")

    return total


answer = roman_to_integer(input("Enter a Roman numeral: "))
print("Answer:", answer)