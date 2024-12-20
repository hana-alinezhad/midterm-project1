a = [ 10 , 20 , 30 ]
b = [ 1 , 2 , 3 , 4]
c = [20 , 40 ]
func = list(map(lambda x , y , z : x * y + z , a , b , c))
for numbers in func:
    print(numbers)