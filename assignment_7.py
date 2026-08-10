book_names= input("enter books name using spaces:")
book_list = book_names.split()
print("books list:",book_list)
print("first book in the list:",book_list[0])
print("last book in the list:",book_list[-1])
print("first three books in the list:",book_list[0:3])
books_title = "python java c++ html css javascript"
print(books_title.upper())
print(books_title.lower())
print(books_title.title())
print(books_title.replace("python","c#"))
print(books_title.split(" "))
print(books_title.strip())
#string = "python"
#string.insert(0,"java")3 string is immutable so we cannot insert any value in it
available_books = ["python","java","c++","html","css","javascript"]
print("available books:",available_books)
available_books.append("c#")
print("available books after appending:",available_books)
available_books.insert(0,"php")
print("available books after inserting:",available_books)
available_books .remove("c++")
print("available books after removing:",available_books)
available_books.pop(1)
print("available books after poping:",available_books)
available_books.sort()
print("available books after sorting:",available_books) 
available_books.reverse()
print("available books after reversing:",available_books)
catogories = ("programming","web development","data science","machine learning ","artificial intelligence")
cat1,cat2,cat3,cat4,cat5 = catogories
print("catogorie1:",cat1)
print("catogorie2:",cat2)
print("catogorie3:",cat3)
print("catogorie4:",cat4)
print("catogorie5:",cat5)
book_geners = {"programming","web development"}
book_geners.add("data science")
print("book geners after adding:",book_geners)
book_geners.remove("web development")
print("book geners after removing:",book_geners)
other_geners = {"programming","machine learning","artificial intelligence"}
print("other geners:",other_geners)
print("union of book geners and other geners:",book_geners.union(other_geners)) 
print("intersection of book geners and other geners:",book_geners.intersection(other_geners))
book = {"book_id": 101,"title": "Python Basics","author": "John"}
print("book title:",book["title"])
print("keys in the book dictionary:",book.keys())
print("values in the book dictionary:",book.values())
print("items in the book dictionary:",book.items())
print("book dictionary after adding new key-value pair:",book.update({"price": 10.99}))
print("book price:",book.get("price"))
book.pop("author")
print("book dictionary after removing author:",book)
library = {101: {"title": "Python", "author": "Alex"},102: {"title": "Java", "author": "David"}}
print("library:",library)
print("book with id 101:",library[101])
print("book title with id 102:",library[102])
print("library keys:",library.keys())
print("library values:",library.values())   
print("library items:",library.items())
print("author in the library:",library[101]["author"])





