import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


numsteps = 10000
rho = 28
sigma = 10
beta = 8/3
h = 0.01
state = np.array([0.0, 1, -1])


def lorenzsystem(state):
    x, y, z = state
    
    x_dot = sigma*(y-x)
    y_dot = x*(rho - z) - y
    z_dot = x*y - beta*z
    
    return np.array([x_dot, y_dot, z_dot])

def rungekutta4(state, h):
    k_1 = lorenzsystem(state)
    k_2 = lorenzsystem(state + k_1 * h/2)
    k_3 = lorenzsystem(state + k_2 * h/2)
    k_4 = lorenzsystem(state + k_3 * h)

    new_state = state + h/6 * (k_1 + 2*k_2 + 2*k_3 + k_4)

    return new_state


traj = np.zeros([numsteps, 3])
traj[0] = state 


#not iterable 
for i in range(1, numsteps):
    traj[i] = rungekutta4(traj[i-1],h)

#next steps are to add time step for loop, so far, rk4 method needs to be validated and tested against true lorenzsystem trajectory
x_plt = traj[:,0]
y_plt = traj[:,1]
z_plt = traj[:,2]

fig1 = plt.figure(figsize=(10,7))
ax = fig1.add_subplot(111, projection='3d')

ax.plot(x_plt, y_plt, z_plt)
plt.show()

time = np.arange(numsteps) * h

fig2, axes = plt.subplots(3, 1, figsize=(10,9))

axes[0].plot(time, x_plt, color='red')
axes[1].plot(time, y_plt, color='green')
axes[2].plot(time, z_plt, color='blue')
plt.show()































"""

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
plt.show()"""
