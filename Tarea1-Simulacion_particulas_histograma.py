import matplotlib.pyplot as plt
import random

def hop(n):
    s = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,n,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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

x = hop(100)
y = sum(x)
list1 = []
for k in range(0,ls):
    list1.append(k)
print(list1)
plt.hist(x,list1)
plt.show()

