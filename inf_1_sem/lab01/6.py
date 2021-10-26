import numpy as np
import matplotlib.pyplot as plt


b = 0.5
a = 3 

def sun(xf):
    
    s = 0
    
    for i in range(1000):
        s = s + np.power(b,i)*np.cos(np.power(a,i)*np.pi*xf)
    return s




x = np.arange(-2, 2, 0.001)


plt.plot(x, sun(x))
plt.show()

