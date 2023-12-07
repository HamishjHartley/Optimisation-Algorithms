from optproblems import cec2005
import numpy as np
import random
from sympy import *


n_dimensions = 10

n_iterations = 100
a = 0.01

#Defining optimisation problem used
function = cec2005.F2(n_dimensions)
x = symbols("x")
y = 5*sin(x)

#Global optima for a given optimisation function
global_optima = function(function.offsets[0:n_dimensions])

#x = random intial vector
initial_vector = np.random.randint(function.min_bounds, function.max_bounds,n_dimensions,dtype=int)
rand = random.randrange(0,1)

#repeat until x is ideal solution 
for i in range(n_iterations):
#     #x = x+ a * derivative of function(x)
    rand = rand + a * y.diff(x)
    print(rand)

print("done")

#