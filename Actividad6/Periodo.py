
# coding: utf-8

# In[1]:

from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()

g = 9.8
#Vectores vacios de abscisas y ordenadas.
x=[]
Ts=[]
i = 0 


# La variable i toma valores de 0 a 90 (grados) en este ciclo.
while (i<=90):
    i = i + 1 
    #convertir grados a radianes
    theta0 = (i*np.pi)/180
    #longitud del pendulo
    l = 1  
    #se define la ecuacion integrar
    f = lambda x: 1/np.sqrt(np.cos(x) - np.cos(theta0)) 
    # Se calcula el valor de la integral
    F, erri = integrate.quad(f,0,theta0)
    T = 4 * np.sqrt(l/g) * (1/np.sqrt(2)) * F
    # Se agrega la abscisa actual al vector de abscisas.
    x.append(i)
    
    # Para graficar Ts/Ths (relación entre periodo real y periodo de oscilaciones pequeñas)
    Ths = 2*np.pi*np.sqrt(l/g)
    T = T/Ths
    # Se agrega la ordenada actual al vector de ordenadas.
    Ts.append(T)

plt.xlabel('Theta0 (grados)')
plt.ylabel('T/T0') 
plt.plot(x,Ts,color='r')
plt.show()


# In[ ]:




# In[ ]:



