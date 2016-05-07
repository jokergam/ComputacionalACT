
# coding: utf-8

# In[34]:

from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
g=9.8

def pend(y, t, b, c):
        theta, omega = y
        dydt = [omega, -b*omega - c*np.sin(theta)]
        return dydt
    
#coeficiente de amortiguamiento    
b = 0.5
#longitud del péndulo
l=2.0
c = g/l
#[angulo inicial, velocidad inicial]
y0 = [np.pi/2.0, 5.0]
t = np.linspace(0, 16, 101)

#solucion
sol = odeint(pend, y0, t, args=(b, c))
        
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()


# In[ ]:



