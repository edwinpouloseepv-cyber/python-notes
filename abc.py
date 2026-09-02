words = input("Enter a string: ")
list = [" ",".",",","!",":",";","?","-"]
wordss =  ""
wordsss = []
for word in words:
    if word not in list:
        wordss += word
    else:
        wordsss.append(wordss)
        wordss = ""
wordsss.append(wordss)
print(max(len(wordsss))) 

