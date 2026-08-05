def total(*number):
    result = 0
    for n in number:
        result += n
    return result
print(total(10,20))
print(total(10,20,30))
print(total(10,20,30,40))