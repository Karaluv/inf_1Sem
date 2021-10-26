import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)

f = input()

plt.plot(x, eval(f))
plt.show()
