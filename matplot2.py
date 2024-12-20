# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:45:12 2024

@author: Hana
"""

import numpy as np
import matplotlib.pyplot as plt

x_positive = np.arange(0.1, 5, 0.1)  
x_negative = np.arange(-5, -0.1, 0.1) 
y1_positive = x_positive**2
y1_negative =x_negative **2
y2_positive = 1/x_positive
y2_negative = 1/x_negative

fig, (a, b) = plt.subplots(2, 1, figsize=(8, 10))
a.plot(x, y1, label='y = x^2', color='greeen')
a.set_title('x^2 function')
a.set_xlabel('x')
a.set_ylabel('y')
a.grid()
a.legend()

b.plot(x, y2, label='y = 1/x', color='red')
b.set_title('1/x function')
b.set_xlabel('x')
b.set_ylabel(' y')
b.grid()
b.legend()

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
plt.show()