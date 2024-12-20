def func1():
    x = "Hana"
    def func2():
        nonlocal x 
        x = "Hello"
    func2()
    return x
print(func1())