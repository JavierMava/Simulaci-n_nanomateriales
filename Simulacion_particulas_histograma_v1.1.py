import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint



def eventos(n):
    s = [0,0,0,0,0,0,0,0,0,0,n,0,0,0,0,0,0,0,0,0,0]
    global ls
    ls = len(s)
    i = 0
    while i < 100:
        for j in range(0,int(len(s))):
            if s[j] != 0 :
                pr = random.random()
                pl = 1 - pr
                if j - 1 < 0:
                    s[j+1] = s[j+1]+int(s[j]*pr)
                    s[j] = s[j] - int(s[j]*pr)
                elif len(s) <= j+1:
                    s[j-1] = s[j-1] + int(s[j]*pl)
                    s[j] = s[j] - int(s[j]*pl)
                else:
                    s[j-1] = s[j-1] + int(s[j]*pl)
                    s[j+1] = s[j+1] + int(s[j]*pr)
                    s[j] = s[j] - int(s[j]*pr) - int(s[j]*pl)
                j+=1
            elif s[j] == 0:
                s[j] = 0
                j+=1
        i+=1
    return s



fig, ax = plt.subplots(figsize=(10, 8))


x = eventos(randint(0,100))
xs = np.arange (len(x))


width = 100
y = sum(x)

ax.plot(y, label= 'Numero de eventos') #corregir

dist = []
for k in range(0,ls):
    dist.append(k)
print(dist)
print(y)



plt.bar(xs,x,dist) 

ax.grid(True)

ax.legend(loc='best')
ax.set_title('Simulacion particulas')
ax.set_xlabel('Eventos')
#ax.set_ylabel('x')

plt.show()

