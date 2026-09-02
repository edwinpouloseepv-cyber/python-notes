numb = int(input("Enter numbers: "))
nums = str(numb)
frequency = {}
for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)
max =0
freq= ""
for key,value in frequency.items():
    if max < value:
        max = value
        freq = key
print("The most frequent number is:", freq)