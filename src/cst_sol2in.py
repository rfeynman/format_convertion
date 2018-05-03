'''
Created on Apr 14, 2014

@author: wange
'''
'''
Created on Mar 10, 2014

@author: wange
generate solinoid field from cst to impactt
'''

import os
import math
import numpy as np
import pprint
#os.rename('solenoid1.txt','1T1.T7'+'~')
if os.path.isfile('1T10.T7'):
    os.remove('1T10.T7')

des=open('1T10.T7','w')
sou=open('bigs.txt','r')

coord=sou.readline()

coord=coord.split()
p_z=int(coord[0])#z grid
p_y=int(coord[1])#y grid
p_x=int(coord[2])#x grid

sep=sou.readlines()
#newline=[None]*len(sep)


d3matrix=np.array([[[None]*p_z]*p_y]*p_x)
#pprint.pprint(matrix)
i=0
j=0
k=0
a=0
print len(sep)
for i in range(0,p_x):
    for j in range(0,p_y):
        for k in range(0,p_z):
            d3matrix[i,j,k]=sep[a]
            a+=1
            #print i,j,k,a,sep[a]
#print d3matrix

i=0
j=0
k=0
new_d3matrix=np.array([[[None]*p_x]*p_y]*p_z)
for i in range(0,p_z):
    for j in range(0,p_y):
        for k in range(0,p_x):
            new_d3matrix[i,j,k]=d3matrix[k,j,i]


print new_d3matrix
#des.write('-0.2   0.2   '+str(p_x-1)+'\n'+'-0.1   0.1   '+str(p_y-1)+'\n'+'-0.3   0.3   '+str(p_z-1)+'\n')# combiner
des.write('-0.106   0.106    '+str(p_x-1)+'\n'+'-0.106    0.106   '+str(p_y-1)+'\n'+'0.773276   2.85328   '+str(p_z-1)+'\n')# dipole
i=0
j=0
k=0
for i in range(0,p_z):
    for j in range(0,p_y):
        for k in range(0,p_x):  
            listline=new_d3matrix[i,j,k].split()
       
            listline[0]='0.00'
            listline[1]='0.00'
            listline[2]='0.00'
      
            '''
            listline[3]=str(float(listline[3])/10000.0)#turn on if CGS
            listline[4]=str(float(listline[4])/10000.0)
            listline[5]=str(float(listline[5])/10000.0)
            '''    
          
          
            jline='    '.join(listline)
            des.write(jline+'\n')             
des.close()
sou.close()