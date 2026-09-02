words = (input("Enter a string: "))
frequency = {}
for char in words:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)
max =0
freq= ""
for key,value in frequency.items():
    if max < value:
        max = value
        freq = key
print("The most frequent character is:", freq, "=", max)