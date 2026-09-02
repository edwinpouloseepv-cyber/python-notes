# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c = a / b
# print("Result:", c)

# print("start")
# print(10 / 0)
# print("end")

# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print("cannot divide by zero")
# except Exception as e:
#     print("Unexpected error:", e)
# else:
#     print("Result:", result)
# finally:
#     print("cleanup complete")

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("error occurred inside divide ()")
        raise
try:
    result = divide(10, 0)
    print("Result:", result)
except ZeroDivisionError:
    print("caller the error")