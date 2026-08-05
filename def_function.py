def greet():
    print("hello")
greet()
greet()


def add(a,b):
    return a+b
result = add(10,20)
print(result)

#or

def add(a,b):
    return a+b
print(add(10,20))


def add(a,b):
    print(a+b)
result = add(10,20)
print(result)


def add(a,b):
    print(a+b)
add(10,20)


def add(a,b):
    return a+b,a*b
s,r = add(20,30)
print(s,r)