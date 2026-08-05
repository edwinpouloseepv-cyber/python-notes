person = dict(name = "anita",city = "delhi",age = 25)
print(person)
print(person["name"])
person = { "name":"anita","city":"delhi","age":25}
print(person)
print(person.get("age",0))
person["age"]= 30
print(person["age"])
print(person)
print(person.get("age",0))
person.update({"name":"edwin"})
print(person)
person.update({"course":"python fullstack"})
print(person)
person.pop("course")
print(person)
person.popitem()
print(person) 
del person["city"]
print(person)

print(person.keys())
print(person.values())
print(person.items())
person = { "name":"anita","city":"delhi","age":25}
for key in person:
    print(key)
for value in person.values():
    print(value)
for key,value in person.items():
    print(key,value)
print("name"in person)

data = {1:"one","two":2,(3,4):"tuple"}
print(data)
#nested dictionary
student = {"name":"rahul","marks":{"maths":90,"science":85}}
print(student["marks"]["maths"])
