'''
Created on Aug 15, 2017

@author: wange
'''
import numpy as np
from numpy import genfromtxt, dtype, loadtxt
import string
from itertools import tee
import pandas as pd


def importdata():
    screendata=genfromtxt('../screen.txt',names=True,dtype=None)
    #print(screendata)
    chgcol=screendata['position']
    jumpind=[]
    for i in range(len(chgcol)-1):
        if chgcol[i]<chgcol[i+1]:
            jumpind.append(i)
        i+=1
    revjumpind=np.array(jumpind[::-1])
    #chgcol_jump=lambda x: chgcol[x], revjumpind
    chgcol_jump=chgcol[revjumpind+1]
    np.append(revjumpind,0)
    chgcol_new=chgcol
    for i in range(len(revjumpind)):
        ind=revjumpind[i]
       
        chgcol_new[0:ind+1]= chgcol[0:ind+1]+chgcol_jump[i]
        #print(np.sum(chgcol_jump[i:]))
        i+=1
    
    #print(chgcol_new,'\n')  
    #print(screendata)
    firstline=screendata.dtype.names
    #print(list(firstline))
    #screendata['position']=chgcol_new
    #print(screendata)
    
    with open('screen_new.txt','wb' ) as cvs:
        #cvs.write(str(firstline)+'\n')
        savehead=list(firstline)
        print(savehead)
        np.savetxt(cvs,screendata,header=savehead,comments='',fmt="%.3e")
    

def main():
    importdata()

if __name__ == '__main__':
    main()