'''
Created on Feb 24, 2014

@author: wange
'''
import numpy as np
import matplotlib.pyplot as plt
import pylab

data=open('fort.18','r')
lines=data.readlines()


#sepd=data.read().split('\n')
#a=sepd[1].split('   ')
#print a[2]

#print sepd.row.split(' ')
x1=[]
y1=[]

for line in lines:
    
    p=line.split()
    x1.append(float(p[1]))
    y1.append(float(p[3]))

xv=np.array(x1)
yv=np.array(y1)

fig=plt.plot(xv,yv)
plt.show()