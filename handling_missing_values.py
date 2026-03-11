#if we wont handle missing values proprly then ml algorithms get failed
'''
np.isnan()-->detect missing values
np.nan_to_num() -->do replace missing values with some number
np.isinf() -->infinite missing values

nan mean not a number(return boolean values)

'''
import numpy as np
a1=np.array([1,np.nan,2,np.nan,3,4,5,np.nan])
print(np.isnan(a1))
print(np.isnan(a1).sum())  #returns the places where there are nan values

print(np.nan_to_num(a1,20))
print(np.nan_to_num(a1,nan=20))

a3=np.array([1,2,np.inf,4,-np.inf])
print(np.isinf(a3))  #true mean positive and negative

cleaned_arr=np.nan_to_num(a3,fposinf=100,neginf=1000)
print(cleaned_arr)