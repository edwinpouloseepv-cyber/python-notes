class student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)
s = student("james")
s.show()
s1 = student("john")
s1.show()