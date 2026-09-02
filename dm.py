char = input("Enter a string: ")
frequency = {}
for count in char:
    if count in frequency:
        frequency[count] += 1
    else:
        frequency[count] = 1
print(frequency)
freq_value = frequency[0]
print(freq_value)