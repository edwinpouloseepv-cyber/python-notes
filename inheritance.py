#1 single inheritance
# class Animal:
#     def speak(self):
#         print("Animal make a sound")

# class Dog(Animal):
#     def bark(self):
#         print("Dog bark")
# d = Dog()
# d.speak()
# d.bark()
#2 multiple inheritance
# class Animal:
#      def speak(self):
#          print("Animal make a sound")
# class Dog(Animal):
#      def bark(self):
#          print("Dog bark")
# class Puppy(Dog):
#      def cry(self):
#           print("puppy cries")
# p = Puppy()
# p.speak()
# p.bark()
# p.cry()
#3 Hierarchial inheritance
# class Animal:
#       def speak(self):
#           print("Animal make a sound")
# class Dog(Animal):
#       def bark(self):
#           print("Dog bark")
# class cat(Animal):
#      def meow(self):
#           print("cat meows")
# d = Dog()
# d.speak()
# d.bark()
# c = cat()
# c.speak()
# c.meow()        
#4 multiple inheritance
# class Father:
#     def drive(self):
#         print("driving a car")

# class Mother:
#     def cook(self):
#         print("cooking food")
# class Child(Father,Mother):
#     pass
# c = Child()
# c.drive()
# c.cook()
#1
# class Vehicle:
#     def Display_Details(self):
#         print("brand : mahindra")
#         print("price : 100000")
# class Car(Vehicle):
#     def Numbers_Of_doors(self):
#         print("Droos : 4 ")
# c = Car()
# c.Display_Details()
# c.Numbers_Of_doors()              
#2 
# class Vehicle():
#     def Brand(self):
#         print("mahindra")
# class Car(Vehicle):
#     def model(self):
#         print("Thar")
# class ElectricCar(Car):
#     def battery_capacity(self):
#         print("10000 KWH")
# e = ElectricCar()
# e.Brand()
# e.model()
# e.battery_capacity() 
#3
class Employee:
    def parent(self):
        self.name = "ramu"
        self.salary ="5000"
class Developer(Employee):
    def programming_language(self):
        print("Employee name :",self.name)
        print("salary:",self.salary)
        print("programing language : python")
class Designer(Employee):
    def desgin(self):
        print("Employee name :",self.name)
        print("salary:",self.salary)
        print("design tool: adob illustrater")
d = Developer()
d.programming_language()               