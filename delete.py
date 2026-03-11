'''
np.delete(array_name,index,axis=None)
flatten array
gives 1d array

'''

import numpy as np 

a1=np.array([10,20,30,40])
print(np.delete(a1,2))

a2=np.array([[1,2,3],[4,5,6]])
print(np.delete(a2,0,axis=0))  #entire 0 row
print(np.delete(a2,(0,1)))  #it delete multiple elements at one time 




