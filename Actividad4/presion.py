
# coding: utf-8

# In[18]:

import numpy as np
from numpy import *
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#"tvsa" es el archivo temperatura en invierno en Nueva York
x, y = loadtxt('pvsa.dat', unpack=True)


def func(x, a, b, c, d):
    return a*np.exp(-c*(x-b))+d
popt, pcov = curve_fit(func, x, y)

plt.plot(x,y,'or',label='data')

plt.plot(x,func(x,*popt),label='fit')
plt.ylabel('presion (mb)')
plt.xlabel('altura (km)')
plt.legend()
plt.show()


# In[ ]:



