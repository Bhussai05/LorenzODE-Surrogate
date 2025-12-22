import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


rho = 28
sigma = 10
beta = 8/3
dt = 0.01
state = np.array([0.0, 1, -1])


def lorenzsystem(state):
    x, y, z = state
    
    x_dot = sigma*(y-x)
    y_dot = x*(rho - z) - y
    z_dot = x*y - beta*z
    
    return np.array([x_dot, y_dot, z_dot])



def simplefunction(x, y):
    z = ((x+1) + np.sin(y))
    return z

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

X, Y = np.meshgrid(x, y)
Z = simplefunction(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

dx, dy, dz = lorenzsystem(state)
print(dx, dy, dz)
        

