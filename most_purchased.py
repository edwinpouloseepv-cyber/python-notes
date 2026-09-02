orders = ["Laptop", "Mouse", "Laptop", "Keyboard","Mouse", "Laptop"]
frequency = {}
for order in orders:
    if order in frequency:
        frequency[order] += 1
    else:
        frequency[order] = 1
max_frequency = 0
most_purchased = ""
for product, count in frequency.items():
    if count > max_frequency:
        max_frequency = count
        most_purchased = product
print(f"The most purchased item is: {most_purchased} with a frequency of {max_frequency}.")