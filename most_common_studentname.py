names = ["Anu", "Rahul", "Anu", "Meera", "Rahul", "Anu"]
frequency = {}
for name in names:
    if name in frequency:
        frequency[name] += 1
    else:
        frequency[name] = 1
count_value = 0
count_key = ""
for key, value in frequency.items():
    if value > count_value:
        count_value = value
        count_key = key        
print(f"The most common student name is: {count_key} with a frequency of {count_value}.")