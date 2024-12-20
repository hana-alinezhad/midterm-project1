def a(n):
    def b(x):
        return x*n
    return b 
times3 = a(3)
times5 = a(5)
print(times3(9))
print(times5(27))
