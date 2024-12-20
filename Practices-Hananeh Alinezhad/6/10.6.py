def a():
    global s
    print(s)
    
    s = " Hello world "
    print(s)
    
s = " It's me"
a()
print(s)