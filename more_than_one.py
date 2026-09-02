char = input("Enter a string: ")
frequency = {}
for count in char:
    if count in frequency:
        frequency[count] += 1
    else:
        frequency[count] = 1
for key, value in frequency.items():
    if value > 1:
        print(f"The character '{key}' appears {value} times.")

