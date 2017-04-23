import pandas as pd
import numpy as np

import time

mylist = ['a','b','c']

letters = pd.Series(mylist)
print("Index are automatically created ")
print("Pandas series \n", letters)

letDict = { 'a': 'Alpha', 'b':'Beta', 'c': 'Gamma'}
letters2 = pd.Series(letDict)
print("Indexes are set through Dictionary")
print("Series Dict \n", letters2)

list1 = ['Alpha', 'Beta', 'Gamma']
list2 = ['a','b','c']
letters3 = pd.Series(list1,list2)
print("Another way to specifiy index values")
print("Series Dict\n")

arr1 = np.array(list(x for x in range(0,20,2)))
ser1 = pd.Series(x for x in range(0,20,2))
print("Array in numpy vs Series in Panda")
print("Numpy Array", arr1, np.sum(arr1))
print("Panda Series", ser1, np.sum(ser1))


print("Processing Times Simple addition vs Numpy Arrays vs Pandas Series")
arr1= np.arange(0,10000,2)
ser1 = pd.Series(list(arr1))
start=time.clock();
sum=0
for idx in arr1:
    sum+=idx
end=time.clock()
print("Simple Add time taken {:2e}".format(end-start) )
start=time.clock();
sum=np.sum(arr1)
end=time.clock()
print("Numpy Array time taken {:2e}".format(end-start) )
start=time.clock();
sum=np.sum(ser1)
end=time.clock()
print("Pandas Series time taken {:2e}".format(end-start) )


print("\n Non-Unique Indices for series")
ser2 = pd.Series(["alpha",'beta','gamma'], index=['a','a','b'])
print(ser2)
print(ser2['a'], ser2['b'])

print("\n Simple math operations similar to numpy arrays")
ser3= pd.Series([1,2,3,4])
print("Add 2 to elements:",ser3+2)
print("Square all elements:",ser3**2)

print("\n Derive a numpy array from Panda series")
arr3 = ser3.values
print("type ", type(arr3),type(arr3indx))