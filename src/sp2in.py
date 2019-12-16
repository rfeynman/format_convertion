'''
Created on Apr 21, 2014

@author: wange
'''

import os
import math

if os.path.isfile('1T6.T7'):
    os.remove('1T6.T7')
des=open('1T6.T7','w')
sou=open('../2956.T7','r')
for i in range(3):
    des.write(sou.readline())
    i+=1
newarray=sou.readlines()
#print newarray[0]

for ele in newarray:
    print( i)
    a=ele.split()
   # print a
    des.write(a[0]+'   '+a[1]+'    '+a[2]+'\n'+a[3]+'\n')
des.close()
sou.close()