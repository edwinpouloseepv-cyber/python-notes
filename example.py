# class Example:
#     public = 1
#     _protected = 2
#     __private = 3
#     def show(self):
#         print(self.__private)


# e = Example()
# print(e.public)
# print(e._protected)
# # print(e.__private)
# e.show()
class A:
    def show(self):
        print("A") 
class B(A): 
    pass
class C(A):
    def show(self):
        print("C") 
class D(B, C):
    pass 
d = D() 
d.show() 