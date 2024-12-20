import math

numbers = [ -3.5 , -7 , 9]
absoloute_value = map(lambda x :math.fabs(x) , numbers)
for numbers in absoloute_value:
    print(numbers)