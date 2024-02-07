import math
from scipy.integrate import quad
def f(x:float) -> float:
    return math.sin(x)
area,error=quad(f,0,math.pi/2)
print(f"Area:{area}")
print(f"Error:{error}")