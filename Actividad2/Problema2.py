
# coding: utf-8

# In[16]:

from math import pi
print ("Este programa le da la altura a la que se encuentra un determinado satelite de la superficie Terrestre")
T = float(input("Escriba el periodo (segundos) del satelite que orbita la Tierra:"))
h = (((3.983324e+14)*(T*T))/(4*pi*pi))**(1.0/3.0)-6371000
print ("La altura a la que se encuentra el satélite es de", h/1000.0, "km")


# In[ ]:



