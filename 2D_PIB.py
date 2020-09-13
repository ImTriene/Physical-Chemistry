import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.pyplot as plt

# Want to create a contour map for the PIB two dimensional wavefunction.


# Principle quantum numbers. Can be changed to visualize the values you want.
n_x = 2
n_y = 3

# Each length respectively, dealing with a 1x1 "box".
L_x = 1
L_y = 1


# Defining the wavefunction

def psi(x, y):
    return (2 / L_x)**(1/2) * np.sin((n_x * np.pi * x)/ L_x) * (2 / L_y)**(1/2) * np.sin((n_y * np.pi * y)/ L_y)

# Defining the probability density
def psi2(x, y):
    return ((2 / L_x)**(1/2) * np.sin((n_x * np.pi * x)/ L_x) * (2 / L_y)**(1/2) * np.sin((n_y * np.pi * y)/ L_y))**2

# Setting values for x and y
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)

X, Y = np.meshgrid(x, y) # Meshgrid creates a rectangular grid out of two given one-dimensional arrays. 
B = psi(X, Y)
Z = psi2(X, Y) #for surface, z must be 2 dimensional

# Plotting the function as a surface plot
fig = plt.figure(1)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap = 'viridis', edgecolor='none') 
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_zlabel(r"$\psi$")
ax.set_title('Surface Map for a 2D Particle in a Box Wavefunction')
plt.show()


fig = plt.figure(2)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, B, rstride=1, cstride=1, cmap = 'viridis', edgecolor='none') 
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_zlabel(r"$\psi^2$")
ax.set_title('Probability density surface map for a 2D Particle in a Box Wavefunction')
plt.show()
