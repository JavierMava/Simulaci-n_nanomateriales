import matplotlib.pyplot as plt
import random
from random import randint
from math import sqrt



def evento(n):
    pr = []
    h = []
    n = randint(50,100)
    d = 3
    p = 5
    l = 100
    for x in range(n):
        particulas = [random.randrange(-l,l,p) for y in range (d)]
        pr.append(particulas)


    for particulas in pr:
        s = sqrt(sum([x**2 for x in particulas]))
        h.append(s)    
    return h







x = evento(randint(0,100))
plt.hist(x,len(x),(0,150))
plt.show()
