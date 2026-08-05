# check Even or Odd
print("enter any number to check odd or even")
def even_or_odd():
    num = int(input("enter the value:"))
    if num %2==0:
        print(num,"is an even number")
    else:
        print(num,"is an odd number")
    return num
even_or_odd() 

# or
print("enter any number to check odd or even")
def even_or_odd(num):
    if num %2 ==0:
        print(num,"is an even number")
    else:
        print(num,"is an odd number")
    return num
even_or_odd(num = int(input("enter any number:")))

# check positive , negative or zero
print("enter any number to check it is positive, negative or zero")
number = int(input("enter any number:"))
if number > 0:
    print("it is an positive number")
elif number < 0:
    print("it is an negative number")
elif number == 0:
    print("number is zero")
else:
    print("invaldi") 


#find the largest of three
print("enter three number to check which is greater")
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if a > b and a > c:
    print(a,"is the largest")
elif b > a and b > c:
    print(b,"is the largest")
else :
    print(c,"is the largest")

#check voting eligibility
print("enter the age to find out the person is eligible for voting or not")
age = int(input("enter your age:"))
if age >= 18 :
    print("you are eligible for voting")
else:
    print("you are not eligible")


#print numbers from 1 to 10
print("printing numbers from one to ten")
for num in range(1,11):
    print(num)

#print even numbers from 1 to 10
print("printing even numbers from 1 to 20")
for num in range(1,21):
    if num %2==0:
        print(num)
# or 
for num in range(2,21,2):
    print(num)


#sum of first n numbers
n = int(input("enter any number:")) 
sum = 0
for i in range(n):
    i = i+1
    sum = sum +i
print(sum)


# multiplication table
num = int(input("enter number:"))
x = 1
for i in range(10):
    i = i + 1
    x = num * i
    print(num,"*",i ,"=",x )

# count from 1 to 10 using while
i = 1
while i <= 10:
    print(i)
    i += 1

# reverse counting
for i in range(10,0,-1):
    print(i) 

#sum until user enter zero

sum = 0
while True:
    num = int(input("enter number to sum:"))
    if num == 0:
        break
    sum += num
    print("sum:",sum)

# skip multiples of three
for i in range(3,11):
    if i % 3 ==0:
        continue
    else :
        print(i) 

# stop at number 7
for i in range(11):
    if i == 8:
        break
    else:
        print(i)


#print only odd number 
for i in range(11):
    if i %2==0:
        continue
    else:
        print(i)

#find factoruial
num = int(input("enter any number to find factorial"))
fact = 1
for i in range(num):
    i =i + 1
    fact = fact * i
print(fact)


#count digits
digits = (1,2,2,2,3,4,5,6,5,6,7,)
print(len(digits))

#reverse a number
num = (input("enter number to reverse :"))
print(num[::-1])


#check palindrom number
num = (input("enter number to reverse :"))
reverse = num[::-1]
if num == reverse:
    print(num,"and it's reverse",reverse,"are same. so it is palindrome" )
else :
    print("it is not palindrome")


#guss the secret number
secret_number = "12345678"
code = input("enter code:")
if code == secret_number:
    print("congratulation your entered code is right ")
else:
    print("wrong code")