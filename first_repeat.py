char = input("enter string:")
frequency = {}
for count in char:
    if count in frequency:
        frequency[count] += 1
    else:
        frequency[count] = 1
first = ""
for key,value in frequency.items():
    if value > 1:
        first = key
        break
print(first)