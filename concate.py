import numpy as np

'''
np.concatenate((a1,a2),axis=0,1)

axis=0 -->up down
axis=1 -->side by side

'''

a1=np.array([[1,2,3],[4,5,6]])
a2=np.array([[10,20,30],[40,50,60]])
print(a1)
print(a2)

a3=np.concatenate((a1,a2),axis=0)
print(a3)

a4=np.concatenate((a1,a2),axis=1)
print(a4)

