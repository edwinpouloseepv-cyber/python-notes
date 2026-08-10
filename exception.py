try:
    f = open("file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    f.close()