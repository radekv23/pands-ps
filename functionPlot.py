# Radoslaw Wojtczak - G00352937
# a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes.

#importing matplotlib and numpy 
import numpy as np
import matplotlib.pyplot as plt

# Setting range from 0 to 4
x= np.arange(0,4)

# calculating y values
y = x
y2 = x * x
y3 = x * x * x

# Adding graph title and labels to X and Y axis
plt.title("Function Plot x (green), 2x (red), x2 (blue); range = [0, 4]")
plt.xlabel("x axis") 
plt.ylabel("y axis") 

# plot may or may not plot the lines, depending on the arguments
plt.plot(x,y,'g.')
plt.plot(x,y2,'r.')
plt.plot(x,y3,'b.')

plt.show()
