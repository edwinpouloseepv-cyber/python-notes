num = int(input("Enter a string: "))
nums = str(num)
frequency = {}
for count in nums:
    if count in frequency:
        frequency[count] += 1
    else:
        frequency[count] = 1
print(frequency)
freq_value = 0
freq_key = ""
for key,value in frequency.items():
    if freq_value == 0 or freq_value > value:
        freq_value = value
        freq_key = key
least_freq = []
for key, value in frequency.items():
    if value == freq_value:
        least_freq.append(key)
print(f"The least frequent number is :{least_freq}.")