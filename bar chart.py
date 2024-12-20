import matplotlib.pyplot as plt

left = [ 1,2,3]
height = [ 15,30,45]
tick_label = ['one' , 'two' , 'three']
plt.bar(left , height , tick_label = tick_label , width = 0.5 , color = ['red' ,'blue','green'])
plt.xlabel ('x')
plt.ylabel('y')
plt.title("First Bar chart!!!")
plt.show()

