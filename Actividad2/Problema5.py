
# coding: utf-8

# In[30]:

from math import factorial
cn=0
n=0
while cn <= 1000000:
    cn = (factorial(2*n))/(factorial(n+1)*factorial(n))
    if cn <= 1000000:
        print(cn)
    n += 1
    


# In[ ]:




# In[ ]:




# In[ ]:



