from functools import reduce
#7
numbers = [1 , 11 , 12 , 77 ]
max_value = reduce(lambda x , y : x if x > y else y , numbers)
print(f"maximum value = {max_value}")
#8
summation_of_numbers_1_100 = reduce(lambda x , y : x + y , range(1,101))
print(f"summation_of_numbers_1_100= {summation_of_numbers_1_100}")