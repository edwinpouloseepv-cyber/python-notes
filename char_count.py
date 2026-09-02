char = input("enter a string:")
frequency = {}
for count in char:
    if count in frequency:
        frequency[count] +=1
    else:
        frequency[count] = 1
print(frequency)