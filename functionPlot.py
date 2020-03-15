# Radoslaw Wojtczak - G00352937
# a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes.

#importing matplotlib and numpy
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1.0, 4.0, 100)
g = x**2
h = x**3

plt.plot(x, g,'g.', label="squared")
plt.plot(x, h,'r.', label="**3")
plt.show()

plt.legend()
plt.title("First Plot")
plt.xlabel("x")
plt.ylabel("y")