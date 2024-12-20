import math

#cos
print(math.cos(1))
#arc_cos
print(math.acos(0.5))
#arc_sin
print(math.asin(0.5))
#arc_tan
print(math.atan(1))

#round_upward
print(f"rounf upward {math.ceil(1.6)}")

#Return_the_value_of_the_first_parameter_and_the_sign_of_the_second_parameter
print(f"value of first parameters and sign of second parameter{math.copysign(4 , -2)}")

#radian to degree
print(f"radian to degree{math.degrees(3)}")

#absolute value of a number
print(f"absolute value of a number{math.fabs(-1)}")

#factorial of a number
print(f"factorial{math.factorial(3)}")

#power
print (f"power{math.pow(3 , 2)}")

#number down to the nearest integer
print(f"down to the nearset integer {math.floor(1.4)}")

#remainder of x/y
print(f"remainder {math.fmod(16 , 3)}")

#sum of all items
print(f"summation of all items = {math.fsum([2 , 2])}")

#log(base10)
a = 100
log1 = math.log(a , 10)
print(f"logarithm {a} with base 10 = {log1}")
#log(base'e')
log2 = math.log(a)
print(f"logarithm{a} with base e = {log2}")

#gratest common division
print(f"gratest common division {math.gcd(30 , 20)}")

#distance
print(f"distance{math.dist((0,0) , (2 ,2))}")
