#!/usr/bin/env python
# coding: utf-8

# # Exercici 1
# ### Crea una funció que donat un Array d’una dimensió, et faci un resum estadístic bàsic de les dades. Si detecta que l’array té més d’una dimensió, ha de mostrar un missatge d’error.

# In[1]:


import numpy as np


# In[33]:


def estadistics(x):
    import numpy as np
    if x.ndim > 1:
        print("Error: vector de més d'una dimensió.")
    else:
        print ("Càlcul estadístic")
        
        a = x.mean()
        b = x.min()
        c = x.max()
        d = x.sum()
        e = np.median(x)
        f = np.std(x)
    
        print("Mitjana:", a)
        print("Mínim:",b)
        print("Màxim:",c)
        print("Sumatori:",d)
        print("Mediana:",e)
        print("Desviació estàndard:",f)


# In[54]:


x = np.array([1,4,2,6,3,8,5,9,6])
y = np.array([[(1,4),(2,6)],[(3,8),(5,9)]])
estadistics(y)


# # Exercici 2
# ### Crea una funció que et generi un quadrat NxN de nombres aleatoris entre el 0 i el 100.

# In[41]:


def quadrat_aleatori(N):
    import numpy as np
    quadrat_aleatori =  np.random.random((N,N)) * 100
    print(quadrat_aleatori)


# In[42]:


quadrat_aleatori(4)


# # Exercici 3
# ### Crea una funció que donada una taula de dues dimensions, et calculi els totals per fila i els totals per columna.

# In[141]:


def totals_fila_columna(x):
    if x.ndim != 2:
        print("La taula ha de tenir dues dimensions!")
    else:
        r1 = x.sum(1)[0]
        r2 = x.sum(1)[1]
        print("Suma fila 1:",r1)
        print("Suma fila 2:",r2)
        for i in np.arange((len(x[0,]))):
            print("Suma columna ",i,": ",x.sum(0)[i],sep="")


# In[235]:


a = np.array([(1,4,3,6,5,7,4,6,8,3),(4,2,5,4,2,5,1,89,3,4)])

totals_fila_columna(a)


# # Exercici 4
# ### Implementa manualment una funció que calculi el coeficient de correlació. Informa’t-en sobre els seus usos i interpretació.

# In[233]:


def coef_corr(x):
    x2 = x[0]**2
    y2 = x[1]**2
    xy = x[0]*x[1]
    mx = x.sum(1)[0]/len(x[1,])
    my = x.sum(1)[1]/len(x[1,])
    cov = (xy.sum()/len(xy)) - (mx*my)
    std_x =((x2.sum()/len(x2))-mx**2)**0.5
    std_y =((y2.sum()/len(y2))-my**2)**0.5
    r = cov/(std_x*std_y)
    print("El coeficient de correlació és:",r)


# In[236]:


a = np.array([(1,4,3,2,6,7),(3,8,6,4,12,14)])

coef_corr(a)


# # 
