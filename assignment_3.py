#asking values to users
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per unit: "))
membership_type = input("Enter membership type (Gold/Silver/Regular):")
available_wallet_balance = float(input("Enter available wallet balance: "))
# calculating all values ,assigning discount and delivery charge using if and elif
total_product_cost = quantity * price
print("total product cost :",total_product_cost)
discount = 100
delivery = 10
if membership_type in ["Gold", "gold", "GOLD"]:
    discount = 100
    print("provided discount :",discount)
    delivery = 10
    print("delivery charge : 10")
elif membership_type in ["Silver", "silver", "SILVER"]:
    discount -= 50
    print("provided discount :",discount)
    delivery += 50
    print("delivery charge :",delivery)
elif membership_type in ["Regular","regular","REGULAR"]:
    discount -=50
    print("no discount")
    delivery += 50
    print("delivery charge :",delivery)
GST = (price * 2) / 100
print("GST amount :",GST)
final_amount = (total_product_cost + GST) - discount
print("total bill :",final_amount)
if available_wallet_balance >= final_amount :
    print("wallet balance : true")
else :
    print("wallet balance : false ")
if final_amount >= 1000 and membership_type in ["Gold", "gold", "GOLD"]:
    final_amount -= 10
    print("free delivey")
    print("total bill:",final_amount)
if membership_type == "Regular" or "regular" or "REGULAR":
    regular = True
else:
    regular = False
if not regular :
    print("membership is not regular :",regular)
else:
    print("membership is not regular :",regular)  
print("bitwise operations")#using bitwise operators
a = int(input())
b = int(input())
c = int(input())
print("a & b =",a & b)
print("a | b =",a | b)
print("a ^ b =",a ^ b)
print("a << c =",a << b)
print("a >> c =",a >> c)
# using membership operators
products = ["Rice","rice","RICE", "Sugar","sugar","SUGAR", "Oil","oil","OIL", "Milk","milk","MILK", "Bread","bread","BREAD"]
if product_name in products:
    print(" product is  in the list")
else:
    print("product is not in the list")
# using identity operators
list1 = ["Rice", "Sugar", "Oil", "Milk", "Bread"]        
list2 = ["Rice", "Sugar", "Oil", "Milk", "Bread"]
print("list1 and list2 have same values:",list1==list2)
print("list1 is list2:",list is list2)




        
