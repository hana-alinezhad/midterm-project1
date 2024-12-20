def a():
    x = 77
    def b():
        global x
        x = 78
    print("before calling b:" + str(x))
    print("calling b now:")
    b()
    print("After calling b:" + str(x))
    
    
a()
print("x in main:" + str(x))