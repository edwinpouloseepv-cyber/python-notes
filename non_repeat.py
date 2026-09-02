words = (input("Enter a string: "))
frequency = {}
for char in words:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
for key,value in frequency.items():
    if value == 1:
        print(key)