# class Dog:
#     def speak(self):
#         print("Woof")
# class Cat:
#     def speak(self):
#         print("meow")
# animals = [Dog(),Cat()]
# for a in animals:
#     a.speak()



# class File:
#     def read(self):
#         print("Reading file")
# class Socket:
#     def read(self):
#         print("reading socket")
# def fetch_data(source):
#     source.read()
# fetch_data(File())
# fetch_data(Socket())


# class File:
#  def read(self):
#     print("reading file")   
# class Socket:
#     pass
# def fetch_data(source):
#     source.read()
# fetch_data(File())
# fetch_data(Socket())


#operator overloading

# class point:
#     def __init__(self,x):
#         self.x = x

#     def __add__(self,other):
#         return self.x + other.x
# p1 = point(10)
# p2 = point(20)
# print(p1 + p2)


# class cart:
#     def __init__(self,x):
#         self.x = x
#     def __add__(self,other):
#         return self.x + other.x 
# c1 = cart(15000)
# c2 = cart(30000)
# print(c1 + c2)



# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __ge__(self,age):
#        if age >= 18:


