x = "ab"
def outer():
    global x
    x = "outer"
    def inner():
        x = "inner"
    inner()
    print("x after inner():",x)
outer()
print(x)
