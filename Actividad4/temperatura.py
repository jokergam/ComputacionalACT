
# coding: utf-8

# In[7]:

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from numpy import *

#"tvsa" es el archivo temperatura en invierno en Nueva York
x, y = loadtxt('tvsa.dat', unpack=True)
xn = np.linspace(min(x), max(x), 200)

m, c = np.polyfit(x, y,1)
yn = np.polyval([m, c], xn)

plt.plot(x, y, 'or',label='data')
plt.plot(xn, yn,label='fit')
plt.ylabel('temperatura (F)')
plt.xlabel('años')
plt.legend()
plt.show()


# In[ ]:



