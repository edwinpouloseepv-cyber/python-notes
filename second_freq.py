words = (input("Enter a string: "))
frequency = {}
for char in words:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)
max = 0
second = 0
max_key = ""
second_key = ""
for char in frequency:
    if frequency[char] > max:
        second = max
        second_key = max_key
        max = frequency[char]
    elif frequency[char] > second and frequency[char] != max:
        second = frequency[char]
        second_key = char
print(f"second most frequent character is :{second_key}")        