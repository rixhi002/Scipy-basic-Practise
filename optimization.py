import numpy as np
from scipy.optimize import minimize
def objective(x):
    a=x[0]
    b=x[1]
    return a**2+b**2
def constraint1(x):
    a=x[0]
    b=x[1]
    return a+b-100
cons=[{
    "type":"eq",
    "fun":constraint1
}]
x0=np.array([200,500])
solution=minimize(objective,x0,method="SLSQP",constraints=cons)
print(solution)