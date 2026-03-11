#summorization of data we use agregrate functions
import numpy as np

a1=np.array([[1,2,3],[3,4,5]])

print(a1.sum())
print(a1.prod())
print(a1.cumsum())  #return 1d array
print(a1.cumprod())  #rturn 1d array
print(a1.mean())
print(a1.max())
print(a1.min())
print(a1.var())
print(a1.std())

print(np.sum(a1))
print(np.prod(a1))
print(np.cumsum(a1))  #return 2d array
print(np.cumprod(a1))  #return 1d array
print(np.mean(a1))
print(np.min(a1))
print(np.max(a1))
print(np.var(a1))
print(np.std(a1))

'''
agregrate function along specific row or column
 
axis=0 -->applied column wise(down ean column)
 
axis=1 -->applied row wise(across each row)

'''

print('sum along columns:',a1.sum(axis=0))
print('sum along row:',a1.sum(axis=1))
 