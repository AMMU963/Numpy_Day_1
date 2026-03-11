#multi dimension array
#matrix 
import numpy as np

a1=np.array([[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]])
print(a1)

a2=np.array([[1,2,3],[4,6,5]])
print(a2)

'''
0D-->only one element
1D-->only one row
2D-->row and column
3D-->depth row and column

'''
#braces are vey imp

#indexing
print(a1[0,0,0]) #depth,row,column
print(a1[1::,::,::])
