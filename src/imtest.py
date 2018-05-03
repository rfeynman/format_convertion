'''
Created on Feb 26, 2014

@author: wange
'''
import os
import math
#os.rename('solenoid1.txt','1T1.T7'+'~')
des=open('soltest.T7','w')
sou=open('solenoid111.txt','r')

next(sou)
next(sou)

des.write('      x [in]         y [in]         z [in]    Bx [Vs/m^2]    By [Vs/m^2]    Bz [Vs/m^2] '+'\n'+'----------------------------------------------------------------------\n')
for line in sou:
    ele=line.split()
    '''
    ele.extend([None,None,None])
    ele[0]=str(float(ele[0])*0.0254)
    ele[1]=str(float(ele[1])*0.0254)
    ele[2]=str(float(ele[2])*0.0254)
    bx=ele[3]
    by=ele[4]
    bz=ele[5]
    ele[3]=ex
    ele[4]=ey
    ele[5]=ez
    ele[6]=bx
    ele[7]=by
    ele[8]=bz
    '''
   
 
    ele[3]='0.00'
    ele[4]='0.00'
    ele[5]='0.01'
    jline='   '.join(ele)
    newline=jline+'\n'
    des.write(newline)
des.close()
sou.close()