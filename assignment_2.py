cn = input("enter customer name:")
fin = input("enter food item name:")
q = int(input("enter quantity:"))
ppi = float(input("enter price per item:"))
km = float(input("enter delivery distance in km:"))
print("customer name:",cn)
print("data type :",type(cn))
print("memory location:",id(cn))
print("food item name:",fin)
print("data type :",type(fin))
print("memory location:",id(fin))
print("quantity:",q)
print("data type :",type(q))
print("memory location:",id(q))
print("price per item:",ppi)
print("data type :",type(ppi))
print("memory location:",id(ppi))
print("delivery distance in km:",km)
print("data type :",type(km))
print("memory location:",id(km))
print("total food cost:",q*ppi)
if km > 5:
    dc = 0
    print("delivery is not possible and you have to come and get the food")
elif km >= 4:
    dc = 50
    print("delivery charge:",dc)
elif km >= 3:
    dc = 30
    print("delivery charge:",dc)
elif km >= 2:
    dc = 20
    print("delivery charge:",dc)
elif km <= 1:
    dc = 0
    print("no delivery charge")
print("final bill amount:",(q*ppi)+dc)
print("data type of quantity is integer:",isinstance(q,int))
print("data type of price per item is float:",isinstance(ppi,float))
print("data type of final bill amount is float:",isinstance(((q*ppi)+dc),float)) 

# variables: it is an entity that can stores data values. it can use any name except keywords.
# data types: it is used to define the types of data . the types of data types are int float,complex.
# memory management using id(): it is used to get the memory location of a object stored in a variable.
# type conversion: it is the method used to convert one data type into another.it has two types implicit and explicit type conversion. implicit type conversion is done by python automatically and explicit type conversion is done by user using functions like int(),float(),str() etc.   