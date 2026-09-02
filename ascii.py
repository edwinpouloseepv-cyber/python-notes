#1. Write a Python program to print the ASCII/Unicode value of characters
# char = input("Enter a character: ")
# print(f"The ASCII value of '{char}' is {ord(char)}")

#2. Character to ASCII number
# char = input("Enter a character: ")
# ascii_number = ord(char)
# print(f"The ASCII number of '{char}' is {ascii_number}")

#3. Number to character
# num = int(input("Enter an ASCII number: "))
# char = chr(num)
# print(f"The character of ASCII number {num} is '{char}'")

#4. Print ASCII values of a word
#word = input("Enter a word: ")
#print(f"The ASCII values of '{word}' are: { [ord(c) for c in word] }")

#5. Print characters from ASCII values
#ascii_values = input("Enter ASCII values separated by spaces: ").split()
#characters = [chr(int(value)) for value in ascii_values]
#print(f"The characters of ASCII values {ascii_values} are: {characters}")

#6. Write a program to check whether a character is uppercase using ASCII values.
# char = input("Enter a character: ")
# ascii_value = ord(char)
# if 65 <= ascii_value <= 90:
#     print(f"'{char}' is an uppercase character.")
# else:
#     print(f"'{char}' is not an uppercase character.")

#7. Write a program to check whether a character is lowercase.
# char = input("Enter a character: ")
# ascii_value = ord(char)
# if 97 <= ascii_value <= 122:
#     print(f"'{char}' is a lowercase character.")
# else:
#     print(f"'{char}' is not a lowercase character.")

#8. Write a program to check whether a character is a digit.
# char = input("Enter a character: ")
# ascii_value = ord(char)
# if 48 <= ascii_value <= 57:
#     print(f"'{char}' is a digit.")
# else:
#     print(f"'{char}' is not a digit.")

#9. Count uppercase letters
# text = input("Enter a string: ")
# uppercase_count = sum(1 for c in text if 65 <= ord(c) <= 90)
# print(f"The number of uppercase letters in '{text}' is: {uppercase_count}")   

#10. Count digits
# text = input("Enter a string: ")
# digit_count = sum(1 for c in text if 48 <= ord(c) <= 57)
# print(f"The number of digits in '{text}' is: {digit_count}")  

#11. Write a program that checks whether the given character is a separator.
# char = input("Enter a character: ")
# separators = [' ', '\t', '\n', ',', '.', ';', ':', '!', '?', '-', '_', '(', ')', '[', ']', '{', '}', '"', "'"]
# if char in separators:
#     print(f"'{char}' is a separator.")
# else:
#     print(f"'{char}' is not a separator.")

#12. Count separators comma,hyphen,semicolon.
# text = input("Enter a string: ")
# separator_count = sum(1 for c in text if c in [',', '-', ';'])
# print(f"The number of separators (comma, hyphen, semicolon) in '{text}' is: {separator_count}")

#13. Remove separators manually
# text = input("Enter a string: ")
#words = ""
# separators = [',', '-', ';', ' ', '\t', '\n', '.', ':', '!', '?', '_', '(', ')', '[', ']', '{', '}', '"', "'"]
# for c in text:
#     if c not in separators:
#         words += c
# print(f"The string without separators is: '{words}'")

#14. Replace separators with spaces
# text = input("Enter a string: ")
#words =""
# separators = [',', '-', ';', '\t', '\n', '.', ':', '!', '?', '_', '(', ')', '[', ']', '{', '}', '"', "'"," "]
# for c in text:
#     if c in separators:
#         words += " "
#     else:
#         words += c
# print(f"The string with separators replaced by spaces is: '{words}'") 

#15. Convert sentence into list of words
# words = input("Enter a string: ")
# list = [" ",".",",","!",":",";","?","-"]
# wordss =  ""
# wordsss = []
# for word in words:
#     if word not in list:
#         wordss += word
#     else:
#         wordsss.append(wordss)
#         wordss = ""
# wordsss.append(wordss)
# print(wordsss)

#16. Find the longest word
# Find the longest word
# s=input("enter a string: ")
# words=[]
# word=""
# for char in s:
#     if(char==" "):
#         words.append(word)
#         word=""
#     else:
#         word+=char
# words.append(word)
# longest_word=words[0]
# for word in words:
#     if(len(word)<len(longest_word)):
#         longest_word=word
# print("The longest word in", s, "is", longest_word)

#17. Find the shortest word
# Find the longest word
# s=input("enter a string: ")
# words=[]
# word=""
# for char in s:
#     if(char==" "):
#         words.append(word)
#         word=""
#     else:
#         word+=char
# words.append(word)
# shotest_word=words[0]
# for word in words:
#     if(len(word)<len(shortest_word)):
#         shortest_word=word
# print("The shortest word in", s, "is", shortest_word)

#18. Count words, digits and special characters
# s=input("enter a string: ")
# words=[]
# word=""
# for char in s:
#     if(char==" "):
#         words.append(word)
#         word=""
#     else:
#         word+=char  
# words.append(word)
# count_words=0
# count_digits=0
# count_special_chars=0
# for word in words:
#     count_words+=1
#     for char in word:
#         if(ord(char)>=48 and ord(char)<=57):
#             count_digits+=1
#         elif((ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122)):
#             continue
#         else:
#             count_special_chars+=1
# print("The number of words in", s, "is", count_words)
# print("The number of digits in", s, "is", count_digits)
# print("The number of special characters in", s, "is", count_special_chars)

#19. Extract only numbers
#s=input("enter a string: ")
# nums=""
# for char in s:
#     if(ord(char)>=48 and ord(char)<=57):
#         nums+=char
# print("The numbers in", s, "are", nums)

#20. Extract only alphabets
#s=input("enter a string: ")
# alphabets=""
# for char in s:
#     if(ord(char)>=97 and ord(char)<=122):
#         alphabets += char
# print("The numbers in", s, "are", alphabets)

#21. Count each type of character
# s = input("Enter a string: ")
# alphabets = 0
# digits = 0
# special = 0
# for char in s:
#     if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
#         alphabets += 1
#     elif ord(char) >= 48 and ord(char) <= 57:
#         digits += 1
#     else:
#         special += 1
# print("Alphabets:", alphabets)
# print("Digits:", digits)
# print("Special characters:", special)
