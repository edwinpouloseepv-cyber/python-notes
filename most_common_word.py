words = input("enter words using space:")
wordss = words.split()
frequency = {}
for word in wordss:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)
count_value = 0
count_key = ""
for key,value in frequency.items():
    if value > count_value:
        count_value = value
        count_key = key
print(f"The most common word is: {count_key} with a frequency of {count_value}.")