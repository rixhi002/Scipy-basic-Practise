import numpy as np
from scipy.stats import norm
import numpy as np
distribution=norm(0,2)
array=np.array([-1,0.0,1,2,3])
print(f"Cummilative distribution:{distribution.cdf(array)}")
print(f"PPF: {distribution.ppf(0.5)}")
print(f"Sampled distribution:{distribution.rvs(size=5)}")