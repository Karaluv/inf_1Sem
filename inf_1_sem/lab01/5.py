import numpy as np
import matplotlib.pyplot as plt
import math


x = [1,2,3,4,5,6]
y = [1, 1.42,1.76,2,2.24,2.5]

p,v = np.polyfit(x,y,deg = 1,cov = True)

plt.plot(x,y)

x = np.array(x)

a1=p[0]
a2=p[1]

plt.plot(x,(x * a1 + a2))

print(p)
plt.show()