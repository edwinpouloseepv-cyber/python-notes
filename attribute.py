class Student:
    course = "python"
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
s1 = Student("marko",56)
s2 = Student("raju",64)
print(s1.course,"=",s1.mark)
print(s2.course,"=",s2.mark)
