import numpy as np
import matplotlib.pyplot as plt
%matplotlib
n = np.arange(0, 10)
a = 2**np.log(n)
b = 2**(2**np.log(n))
c = n**(5/2)
d = 2**(n**2)
e = (n**2)*(np.log(n))

plt.plot(n, a)
plt.plot(n, b)
plt.plot(n, c)
plt.plot(n, d)
plt.plot(n, e)
plt.legend(('a', 'b', 'c', 'd', 'e'), loc='upper left')
plt.grid(True)