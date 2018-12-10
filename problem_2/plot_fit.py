import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # projection='3d'

def func(x, y):
    return (1-x)**2*np.exp(-x**2-(y+1)**2)-(x-x**3-y**3)*np.exp(-x**2-y**2)

def func_exp(x, y):
    return np.ceil(np.exp((1-x)**2*np.exp(-x**2-(y+1)**2)-(x-x**3-y**3)*np.exp(-x**2-y**2)))

x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)

X , Y = np.meshgrid(x, y)

Z = func_exp(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z)  # Axes3D.plot_surface(X, Y, Z, *args, **kwargs)
ax.set_title('ceiling of exp(f(x, y))')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')

plt.show()




