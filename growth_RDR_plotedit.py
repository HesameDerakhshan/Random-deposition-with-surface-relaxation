
 #from random import randrange
import random
import matplotlib.pyplot as plt
import numpy as np
import math

H     = []

l     = 200
h     = np.zeros(l)
W_var = []
T     = []
t     = 40000
L     =range(0,l)	
j=1
pp=0
pR=0
pL=0
ccolor="black"
while (j<t):
    #	rand = randrange(l)
    rand = round(np.random.random_sample()  * l)
    minElement = min(h[rand%l],h[(rand-1)%l],h[(rand+1)%l])
#    print(rand)
#    print('min',minElement)
    if (h[rand%l] == minElement):
        h[rand%l]=h[rand%l]+1
        pp+=1  #tetst   
    elif (h[(rand-1)%l] == h[(rand+1)%l]):
        choice = random.choice([rand-1,rand+1])	

        h[(choice)%l]=h[(choice)%l]+1
        
    elif (h[(rand-1)%l] == minElement):
        h[(rand-1)%l]=h[(rand-1)%l]+1
        pL+=1   #tetst
    else:
        h[(rand+1)%l]=h[(rand+1)%l]+1
        pR+=1   #tetst
        
    #	W_var.append(np.var(h))
    #	T.append(j)


    if((j)%5000==0):
        H.append(h)  

    print(j)
    j+=1
H = np.asarray(H)
L = np.asarray(L)
#plt.stackplot(L,H)
plt.stackplot(L,H)

plt.show()
#plt.plot(T,W_var)
#plt.plot(h)



#p = np.polyfit(T,W_var,1) #fit kardan dade ba darage delkhah
#print (h)
#f = np.poly1d(p)
#print (f)
#plt.plot(T,W_var, 'bo', label="Data") # mokhtast data ha
#plt.plot(T,f(T), 'b-',label="Polyfit") # khat fit
#plt.show()
