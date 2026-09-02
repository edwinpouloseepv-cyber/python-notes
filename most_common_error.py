errors = [404, 500, 404, 403, 404, 500]
frequency = {}
for error in errors:
    if error in frequency:
        frequency[error] += 1
    else:
        frequency[error] = 1
count_value = 0
count_key = ""
for key,value in frequency.items():
    if value > count_value:
        count_value = value
        count_key = key
print(f"The most common error is: {count_key}.")