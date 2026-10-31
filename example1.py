class Model:
    def __str__(self):
        return "This is a model object"


class Student(Model):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.email})"


student1 = Student("Anjali", "anjali@gmail.com", 21)

print(student1)
print(Student.__str__)
print(Model.__str__)
print(Model().__str__())