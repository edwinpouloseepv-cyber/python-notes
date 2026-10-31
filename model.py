#print an array, reverse,odd and even from the array
# array = [1,2,3,4,5,6,7,8,9]
# print(" array:", array)
# print("reverse array:",array[::-1])
# print("odd:",[i for i in array if i %2 != 0])
# print("even:",[i for i in array if i %2 == 0])

#print an 2d array,reverse,odd and even from the 2d array
# array2d = [[1,2,3],[4,5,6],[7,8,9]]
# print("2D Array:", array2d)
# print("Reversed 2D Array:", [row[::-1] for row in array2d])
# print("Odd Elements:", [num for row in array2d for num in row if num % 2 != 0])
# print("Even Elements:", [num for row in array2d for num in row if num % 2 == 0])

#program to print pattern
# 1A
# 1A 2B
# 1A 2B 3C
# 1A 2B 3C 4D
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(f"{j}{chr(64+j)}",end=" ")
#     print()

#progrsam to print the subset of ABC
for i in range(1,4):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()
