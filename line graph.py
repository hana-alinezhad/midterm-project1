import matplotlib.pyplot as plt

x1 = [1,3,7]
y1 = [2,4,5]
plt.plot(x1 , y1 , label = "Line1" )

x2=[1,3,5]
y2=[0,4,8]
plt.plot(x2 , y2 , label= "Line2" )

plt.xlabel('x')
plt.ylabel('y')
plt.title("number one")
plt.legend()
plt.show()