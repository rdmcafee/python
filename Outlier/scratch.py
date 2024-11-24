##Outlier ID 6716cc60559f278d6b6e8bbe
import numpy as np
import sympy as sp
from scipy.integrate import dblquad
from sympy import nsolve

'''
def satisfies_relation(a, b):
    #check is a is a multiple of b^2
    return b != 0 and a % (b**2) == 0

# Input two natural numbers from the user
a = int(input("Enter the first natural number A:"))
b= int(input("Enter the second natural number B:"))

# Check if they satisfy the relation R
if satisfies_relation(a, b):
    print(f"The numbers {a} and {b} satisfy the relation R (A is a multiple of B^2).")

else:
    print(f"The numbers {a} and {b} do not satisfy the relation R (A is not a multiple of B^2).")
'''

'''
def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean(b % a, a)
        return gcd, y - (b // a) * x,  x
    
def mod_inverse(a, m):
    gcd, x, y = extended_euclidean(a, m)
    if gcd != 1:
        return None
    else:
        return x % m
    
def find_vertical_asymptotes_and_modular_inverse():
    x = sp.symbols('x')
    equation = (x**2 - 4) * sp.log(x - 1)
    solutions = sp.solve(equation, x)
    print(solutions)

    function = (x**3 - x**2 - 4*x + 4) / (sp.log(x - 1)*(x**2 - 4))
    limit_left = sp.limit(function, x, 2, dir='-')
    limit_right = sp.limit(function, x, 2, dir='+')

    if limit_left.is_infinite or limit_right.is_infinite:
        print("There is a vertical asymptote at x = 2")
        a = 2
        m = 17
        inverse = mod_inverse(a, m)
        #int(f"The modular inverse of {a} modulo {m} is {inverse}")
        print(f"The modular inverse of {a} modulo {m} is {inverse}")
    else:
        print("There is no vertical asymptote at x = 2.")

find_vertical_asymptotes_and_modular_inverse()
'''

'''
#Binomial expansion

def calculate_coefficient_x6():
    # define the variable x
    x = sp.symbols('x')

    # define the generating function for k = 1 to 5
    generating_function = sp.prod([(1 - x**k)**-1 for k in range(1, 6)])

    # Expand the generating function
    expanded_function = sp.series(generating_function, x, 0, 7).removeO()

    # Calculate the coefficient of x^6
    coefficient_x6 = expanded_function.coeff(x**6)

    return(coefficient_x6)

# Execute the function
result = calculate_coefficient_x6()
print(result)
'''
'''
#Derivatives
# Define the variable

u = sp.symbols('u')

# Define the outer function
f_outer = sp.sin(u)

# Calculate the derivative of the outer function
f_outer_prime = sp.diff(f_outer, u)

print(f_outer_prime)

### Compiles correctly up to this point

# Define a new variable
x = sp.symbols('x')

# define the inner function
g = sp.exp(x) - 2*x + 1

# Calculate the derivative of the inner function

g_prime = sp.diff(g, x)

print(g_prime)

### Also correct in the above section (inner function)
'''

'''
# Now combine steps

def evaluate_derivative():
    # Define the variables
    u = sp.symbols('u')
    x = sp.symbols('x')

    # Define the outer function
    f_outer = sp.sin(u)

    # Calculate the derivative of the outer function
    f_outer_prime = sp.diff(f_outer, u)

    # Define the inner function
    g = sp.exp(x) - 2*x + 1

    # Calculate the derivative of the inner function
    g_prime = sp.diff(g, x)

    # Substitue g(x) into the derivative of the outer function
    f_prime = f_outer_prime.subs(u, g)

    # Muiltiply by the derivative of the inner function
    f_prime = f_prime * g_prime

    # Evaluate the derivative at x = 1
    result = f_prime.subs(x, 1)

    return result

# Execute the function
result = evaluate_derivative()
print(result)
'''
'''
def calculate_jacobian_determinant(u, v):
    # Define the partial derivatives
    
    dx_du = 3*u**2 - 3 * v**2
    dx_dv = -6 * u * v
    dy_du = 6 * u * v
    dy_dv = 3 * u**2 - 3 * v**2
    
    # Calculate the jacobian determinant
    J = dx_du * dy_dv - dx_dv * dy_du

    return J

### Ok here we needed to define symbols u and v; the definition above 
### requires symbolic expression be defined as in input. 
u = sp.symbols('u')
v = sp.symbols('v')
h = sp.symbols('h')

J = calculate_jacobian_determinant(u, v)
J = sp.factor(J)
print(J)

# Simplify the expression to be integrated. 
x = sp.symbols('x')
y = sp.symbols('y')
a = sp.symbols('a')

h = sp.sqrt(1-u**2)
v = h

x_func = u**3 - 3*u*v
y_func = 3*u**2 * v - v**3


grandFunc = sp.simplify((x_func**2 + y_func**2) * J)
print(grandFunc)


print(grandFunc)
#gfun = lambda a: -1 * np.sqrt(1-u**2)
#hfun = lambda a: np.sqrt(1-u**2)
def lower_limit():
    return -1 * sp.sqrt(1-u**2)

def upper_limit(): 
    return sp.sqrt(1-u**2)

'''
'''
integrand_result, error = dblquad(grandFunc, 0, 1, lower_limit, upper_limit)
print(integrand_result)
print("error", error)
'''
'''
#integrand_result = 2 * sp.integrate(grandFunc, (v, 0, sp.sqrt(u**2 - 1)), (u, 0, 1))
#print(integrand_result)
#print(type(grandFunc))
'''
'''
def calculate_jacobian_determinant(u, v):
    dx_du = 3*u**2 - 3*v**2
    dx_dv = -6*u*v
    dy_du = 6*u*v
    dy_dv = 3*u**2 - 3*v**2

    J = dx_du*dy_dv - dx_dv*dy_du
    return(J)

def evaluate_jacobian_determinant(u, v):
    J = calculate_jacobian_determinant(u, v)
    return J

def calculate_integrand(u, v):
    x = u**3 - 3*u * v**2
    y = 3 * u**2 + v**2
    integrand = x**2 + y**2

    def jac (u, v):
        return evaluate_jacobian_determinant(u, v)
    J = jac(u, v)

    return J* integrand

def calculate_limits():
    theta_lower = 0
    theta_upper = 2*np.pi
    return theta_lower, theta_upper

def evaluate_double_integral():
    theta_lower, theta_upper = calculate_limits()
    #J = evaluate_jacobian_determinant()
    def integrand(u, v):
        return calculate_integrand(u, v)
    
    result, error = dblquad(integrand, -1, 1, lambda u: -np.sqrt(1 - u**2), lambda u: np.sqrt(1-u**2))
    return result

result = evaluate_double_integral()
print(result)
'''
def find_numerical_critical_points(f_prime, x, initial_guesses):
    critical_points = []
    for guess in initial_guesses:
        try:
            sol = nsolve(f_prime, x, guess)
            sol = sol.evalf()
            if sol.is_real:
                if not any(abs(sol - cp) < 1e-5 for cp in critical_points):
                    critical_points.append(sol)
        except:
            pass
    return critical_points

def analyze_function():
    # Define the variable
    x = sp.symbols('x')

    # Define the function
    f = x**3 - 3*x**2 + 4*sp.sin(x)*sp.exp(-x)

    # Compute the derivative of f
    f_prime = sp.diff(f, x)

    # Find the critical points
    initial_guesses = [0, 1, 2, 3, 4, 5]
    critical_points = find_numerical_critical_points(f_prime, x, initial_guesses)

    # Apply the second derivative test
    f_double_prime = sp.diff(f, x, 2)

    for cp in critical_points:
        value = f_double_prime.subs(x, cp)
        if value < 0:
            print(f"The critical point {cp} corresponds to a local maximum")
        elif value > 0:
            print(f"The critical point {cp} corresponds to a local minimum")
        else:
            print(f"The seconds derivative test is inconclusive for the critical point {cp}")
    
    # Analyze the behavior of f(x) as it approaches +/- infinity
    limit_pos_inf = sp.limit(f, x, sp.oo)
    limit_neg_inf = sp.limit(f, x, -sp.oo)

    print(f"The limit of f(x) as x approaches positive infinity is {limit_pos_inf}.")
    print(f"The limit of f(x) as x approaches negative infinity is {limit_neg_inf}.")

# Execute the function
analyze_function()
print(critical_points)
