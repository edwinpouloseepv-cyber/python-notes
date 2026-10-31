# def Squre(x):          # map
#     return x * x
# numbers = [1, 2, 3, 4, 5]
# result = map(Squre, numbers)
# print(list(result))  # Output: [1, 4, 9, 16, 25]


# def is_even(x):
#     return x % 2 == 0
# numbers = [1, 2, 3, 4, 5, 6]             #filter
# result = filter(is_even, numbers)
# print(list(result))  # Output: [2, 4, 6]


# from functools import reduce
# def multiply(a, b):
#     return a * b                         #reduce
# numbers = [1, 2, 3, 4]
# result = reduce(multiply, numbers)
# print(result)  # Output: 24

# number = [5 ,2 ,8 ,1]
# print(sorted(number))  # Output: [1, 2, 5, 8]



# s = lambda x: x * x
# print(s(5))  # Output: 25


# number = [5, 2, 8, 1]
# result = map(lambda x: x * 2, number)
# print(list(result))  # Output: [10, 4, 16, 2]

# number = [1, 2, 3, 4, 5, 6]
# result = filter(lambda x: x % 2 == 0, number)
# print(list(result))  # Output: [2, 4, 6]