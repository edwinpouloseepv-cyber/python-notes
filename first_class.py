# def Greet():
#     print("Hello, welcome to the first class!")
# # x = Greet   #store a function in a veriable
# # x()
# Greet()


#pass a function as an argument to another function
# def Squre(x):
#     return x * x

# def Calculate(func, value):
#     return func(value)
# result = Calculate(Squre, 5)
# print(result)

#Return a function from another function
# def Outer():
#     def Inner():
#         print("Hello from the inner function!")
#     return Inner
# x = Outer()  # x is now the Inner function
# x()  # Call the inner function