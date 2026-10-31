# from functools import lru_cache
# @lru_cache
# def square(x):
#     print("Calculating .....")
#     return x * x
# print(square(5))
# print(square(5))
# print(square(5))
# print(square(6))


# #  partial function
# from functools import partial
# def power(base, exponent):
#     return base ** exponent
# square = partial(power, exponent=2)
# print(square(4))
# print(square(5))
# print(square(10))

# #list comprehension 
# numbers = [1, 2, 3, 4, 5]
# squares = [x * x for x in numbers]
# print(squares)  
# set comprehension
# numbers = [1, 2, 2, 3 ,3 ,4, 5]
# square = {x * x for x in numbers}
# print(square)  # Output: {1, 4, 9, 16, 25}

# # dictionary comprehension
# numbers = [1, 2, 3, 4, 5]
# square_dict = {x: x * x for x in numbers}
# print(square_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


#generator expression
# numbers = [1 ,2 ,3 ,4]
# square = (x * x for x in numbers)
# print(square)
# print(next(square))
# print(next(square))
# print(list(square))

# # nested comprehension
# matrix = [[1,2], [3,4]]
# result = [x for row in matrix for x in row]
# print(result)  # Output: [1, 2, 3, 4]

# #itratable
# numbers = [1, 2, 3]
# it = iter(numbers)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# #generator
# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1
# numbers = count_up_to(3)
# print(next(numbers))  # Output: 1
# print(next(numbers))  # Output: 2
# print(next(numbers))  # Output: 3
# print(next(numbers))  # Raises StopIteration

#decorator
def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()  # Output: before Hello! after