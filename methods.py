nums = (1,2,2,3)
print(nums.count(2))


nums = (10,20,30)
print(nums.index(20))



colors = ("red","green","blue")
for color in colors:
    print(color)


student = ("Achu",20)
name,age = student
print("Name:",name)
print("age:",age)



numbers = (1,2,3,4,5)
a,b,*c = numbers
print("a=",a)
print("b=",b)
print("c=",c)



num_list=[1,2,3]
num_tuple=tuple(num_list)
print(num_tuple)


num_tuple = (1,2,3,4)
num_list = list(num_tuple)
print(num_list)

data = ((1,2),(3,4))
print(data[1][0])

data = ([1,2],[3,4])
data[0].append(4)
print(data)



numbers = {1,2,3,3,4,5}
print(numbers)


nums = set([1,2,3,4])
print(nums)


numbers = {}
print(type(numbers))
empty = set()
print(type(empty))


numbers ={1,2,3,4}
for i in numbers:
    print(i)



nums = {1,2}
nums.add(3)
print(nums)


nums = {1,2}
nums.update([3,4,5])
print(nums)


nums = {1,2,3}
nums.remove(2)
print(nums)

nums = {1,2}
nums.update({3,4,5})
print(nums)

nums = {1,2,3}
#nums.remove(4)
nums.discard(4)
print(nums)



nums = {1,2,3,4,5,6}
nums.pop()
print(nums)
nums.clear()
print(nums)

#set operations
#1 union

A = {1,2,3}
B = {3,4,5}
c = A | B
print(c)
# intersection
D = A & B
print(D)
# 
E = A - B
print(E)

F = A ^ B
print(F)

#frozenset
nums = frozenset([1,2,3])
print(nums)
# to prevent accidental modification

# membership testing
# membership testing is used to check whether an element is present in a set or not
nums = {1,2,3}
print(2 in nums) 

# dictionary

