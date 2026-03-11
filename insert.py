#to add the data 

import numpy as np

a1=np.array([1,2,4,5,6,7])

'''
inserting

np.insert(array_name,index,value,axis=none)
until and unless we store it they wont moddify the original array

'''
#for 1D
print(np.insert(a1,3,10)) 
print(np.insert(a1,6,4))
print(a1)
print(np.insert(a1,6,[1,2,3])) #pass multiple elements as list

#for 2D array
a2=np.array([[1,2,3],[4,5,6]])
print(a2)
print(np.insert(a2,1,[10,20,30],axis=0)) #up down
print(np.insert(a2,0,[40,50],axis=1))    #ide by side


