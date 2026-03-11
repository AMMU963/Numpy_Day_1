'''
everything in numpy starts from zero

when i want to pick the speciifc element
-->we use indexing

when we want some range of elements
-->we use slicing

-->fancy indexing
-->boolean marking

'''
import numpy as np

a1=np.array([[1,2,3],[4,5,6]])

print(a1[0,0])  #go to files of specific dim

#boolean marking
print(a1>2)
print(a1[a1>2])   


'''
fancy indexing
sleecting multiple elements at one time

'''
a2=np.array([10,20,30])
print(a2[[0,2]])   #inside we pass index


