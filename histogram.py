import matplotlib.pyplot as plt

age = [ 2 ,10 , 32, 25,27]
range = (0, 100)
bin = 4
plt.hist ( age , bin , range  , color ='blue' ,histtype= 'bar' , rwidth= 0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title("First histogram chart")
plt.show()

