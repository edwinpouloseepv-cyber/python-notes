choice=["1.Book Ticket","2.View Seat Availability","3.Cancel Ticket","4.Exit"]
for option in choice:
    print(option)
while choice != 0:
    option = int(input("Enter any option:"))
    if option == 1:
        name = input("enter your name:")
    elif option == 2:
        print("available seats:")
        seat_no = 0
        for seat in range(1,11):
            if seat_no == seat:
                continue
            print(seat)
        seatno = int(input("enter seat number:"))
        seat_no += seatno           
        age = int(input("enter your age:"))
        if age <= 12 or age >=70 :
            print("ticket price: 50" )
        else:
            print("ticket price:200")
    elif option == 3:
        print("your ticket canceled")
    else :
        print("exit")
        break                    
   
