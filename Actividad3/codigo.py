
# coding: utf-8

# ********EJEMPLO********

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Original "data set" --- 21 random numbers between 0 and 1.
x0 = np.linspace(-1,1,21)
y0 = np.random.random(21)

plt.plot(x0, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x = np.linspace(-1,1,101)

# Available options for interp1d
options = ('linear', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic', 10)

for o in options:
    f = interp1d(x0, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()


# ******CASO 1*******

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

# Original "data set" --- 10 random numbers between 0 and 3.
n = np.random.random(10)
x0 = 3.0*n
y0 = np.sin(2.0*x0)

plt.plot(x0, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x = np.linspace(min(x0),max(x0),101)

# Available options for interp1d
options = ('linear',  'quadratic', 'cubic',)

for o in options:
    f = interp1d(x0, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()


# **********CASO 2***********

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

# Original "data set" --- 20 random numbers between -10 and 10.
n = np.random.random(20)
x0 = 20.0*n - 10.0
y0 = np.sin(x0)/x0

plt.plot(x0, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x = np.linspace(min(x0),max(x0),101)

# Available options for interp1d
options = ('linear',  'quadratic', 'cubic',)

for o in options:
    f = interp1d(x0, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()





# **********CASO 3*************

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

# Original "data set" --- 16 random numbers between -3 and 3.
n = np.random.random(16)
x0 = 6.0*n - 3.0
y0 = np.sin(2.0*x0)*x0*x0

plt.plot(x0, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x = np.linspace(min(x0),max(x0),101)

# Available options for interp1d
options = ('linear',  'quadratic', 'cubic',)

for o in options:
    f = interp1d(x0, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()


# In[ ]:




# *********CASO 4************

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

# Original "data set" --- 12 random numbers between -2 and 2.
n = np.random.random(12)
x0 = 4.0*n - 2.0
y0 = np.sin(3.0*x0)*x0**(3.0)

plt.plot(x0, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x = np.linspace(min(x0),max(x0),101)

# Available options for interp1d
options = ('linear',  'quadratic', 'cubic',)

for o in options:
    f = interp1d(x0, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()


# In[ ]:



