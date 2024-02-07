import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 3, 5, 7, 11])

predict = interp1d(X, Y, kind="quadratic")

X2 = np.linspace(np.min(X), np.max(X), 100)
Y2 = np.array([predict(x) for x in X2])

plt.plot(X, Y, "o:")
plt.plot(X2, Y2, "ro:")
plt.show()

print(f"At X = 1.5, Y = {predict(1.5)}")
