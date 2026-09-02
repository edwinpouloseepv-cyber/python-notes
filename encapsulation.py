#Encapsulation

# class Student:
#     def __init__(self):
#         self._marks = 0
#     @property
#     def marks(self):
#         return self._marks
#     @marks.setter
#     def marks(self,value):
#         if value < 0:
#             print("Invalid marks")
#         else :
#             self._marks = value
# s = Student()
# s.marks = 80
# print(s.marks)

# class Student:
#     def __init__(self):
#         self.marks = 80
# s = Student()
# print(s.marks)
# s.marks = 5
# print(s.marks)


# class Student:
#     def __init__(self):
#         self.__marks = 80
#     def my_marks(self):
#         print(self.__marks)
# s = Student()
# s.my_marks()


class Student:
    def __init__(self):
        self.__marks = 80
    def get_marks(self):
        return self.__marks
    def set_marks(self,value):
        if value < 0:
            print("invalid")
        else:
            self.__marks = value
s = Student()
print(s.get_marks())
s.set_marks(-1)
print(s.get_marks())
