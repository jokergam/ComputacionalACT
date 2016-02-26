
# coding: utf-8

# In[9]:

from math import sin,acos,pi,sqrt
x = float(input("Escribe la coordenada x"))
y = float(input("Escribe la coordenada y:"))
z = float(input("Escribe la coordenada z:"))
r = sqrt(x*x+y*y+z*z)
phi = acos(z/r)
theta = acos(x/(r*sin(phi)))
print("r =",r,"phi =",phi*180/pi, "grados", "theta =", theta*180/pi, "grados")


# In[ ]:



