
# coding: utf-8

# In[40]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import *
#parametros
g = 9.81
l = 1.0
c = g/l

X_f1 = np.array([-10*np.pi,10*np.pi])
X_f2 = np.array([-5*np.pi,5*np.pi])
t = np.linspace(0,20,1000)

b=0
#funcion
def pend(y, t, b, c):
    theta, omega = y
    dy_dt = [omega,-c*np.sin(theta)]
    return dy_dt


values  = linspace(-1, 1, 70)                          
vcolors = plt.cm.autumn_r(np.linspace(0.3, 1, len(values)))  
plt.figure(2)

for v, col in zip(values, vcolors):
    y0 = v * X_f1                              
    
    X = odeint(pend, y0, t, args=(b,c))         
    plt.plot( X[:,0], X[:,1], lw=3.5*v, color=col, label='X0=(%.f, %.f)' % ( y0[0], y0[1]) )

                              
for v, col in zip(values, vcolors):
    y1 = v * X_f2                           
    X1 = odeint(pend, y1, t, args=(b,c))           
    plt.plot( X1[:,0], X1[:,1], lw=3.5*v, color=col, label='X0=(%.f, %.f)' % ( y1[0], y1[1]) )

#graficar    
plt.title('Espacio fase')
plt.xlabel('$\\theta$')
plt.ylabel('$\omega$')
plt.grid()
plt.xlim(-3.0*np.pi,3.0*np.pi)
plt.ylim(-15,15)
plt.show()


# In[ ]:



