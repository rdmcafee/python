import numpy as np
import sympy as sp
from scipy.linalg import det
from scipy.integrate import quad
from scipy.integrate import dblquad

# Define variables to be used.
x = sp.symbols('x')
y = sp.symbols('y')

u = sp.symbols('u')
v = sp.symbols('v')
'''
r = sp.symbols('r')
theta = sp.symbols('theta')

x = r*sp.cos(theta)
y = r*sp.sin(theta)

func = x**2 + y**2

dx_dr = sp.diff(x, r)
dx_dtheta = sp.diff(x, theta)

dy_dr = sp.diff(y, r)
dy_dtheta = sp.diff(y, theta)

detMatrix = sp.Matrix([[dx_dr, dx_dtheta], [dy_dr, dy_dtheta]])

j = sp.simplify(sp.det(detMatrix))
print(f"Jacobian = {j} dr_dTheta")

integrand = sp.integrate(func*j, (r, 0, 1), (theta, 0, 2*sp.pi))
print(integrand)
'''

u = (1 - x**2)**0.5
func = x**2 + y**2
integrand = 4 * sp.integrate(func, (y, 0, (1-x**2)**0.5), (x, 0, 1))

print(sp.simplify(integrand))
    
print(np.pi)
print(0.8862269*np.sqrt(np.pi))
