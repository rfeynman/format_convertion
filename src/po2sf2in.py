'''
Created on Feb 19, 2014

@author: Erdong
generate a impactt field from possion
'''


import os
import math
# os.rename('1T1.T7','1T1.T7'+'~')
if os.path.isfile('1T1.T7'):
    os.remove('1T1.T7')
des=open('1T1.T7','w')
sou=open('../dcgun_GHV.T7','r')
intervelz=sou.readline()
intervelz=intervelz.split()
#sou.readline()
intervelr=sou.readline()
intervelr=intervelr.split()
sep=sou.readlines()
newline=[None]*(len(sep))
a=0
i=0
print(intervelz)
r=int(intervelr[2]) # r intervel
range_r=intervelr[1]
z=int(intervelz[2]) #z intervel
range_z=intervelz[1]
#print len(sep)
#print sep, len(sep)
for i in range(0,len(sep)):
    k=int(i)/(r+1)
    newline[int(a*(z+1)+k)]=sep[int(i)]
    #print i,' ',a*101+k,'  ',sep[int(i)],' ',newline[a*101+k]
    a=a+1
    if int(i+1)%(r+1)==0:
        a=0

a=newline[1].split()
print (a,   a[1])
#print i,a,k,len(newline),newline[a*101+k],sep[int(i)]
des.write('0.0  '+intervelz[1]+'  '+intervelz[2]+'\n'+'0.00 \n'+'0.0  '+intervelr[1]+'  '+intervelr[2]+'\n')
for ele in newline:
    listline=ele.split()
    #print listline
    listline.append('0.00')
    a=listline[0]
    listline[0]=listline[1]
    listline[1]=a
    listline[2]=str(0.000)
    #listline[2]=str(math.sqrt(float(listline[0])**2+float(listline[1])**2))
    jline='    '.join(listline)
    newline=jline.strip()+'\n'+'   0.00000\n'
    des.write(newline)
    #print line
# write( '0.0 6 100\n'+  '0.00\n'+' 0.0 1 30 \n' )
sou.close()
des.close()

