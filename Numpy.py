import numpy as np



mylist = ['a','b','c']
x = np.array(mylist)
print(mylist,x)

x= np.arange(1,20,2)
print('Array ',x,'Length ',len(x))
y = x.reshape(2,5)
print('Reshaped ',y)

print('Slicing')
print (y[:,3])
print (y[1:2,:])

# increment x by 1
x = x +1
print ('Incremented ',x)

# increment selected indices

x[1:5] +=1
print('Inc sel indices', x)

# indexing through another array
indices= np.array([2,3])
y = x[indices]+ 1
print('Indexing with a list',y)

# append to an exiting array
x= np.append(x,[101,102,103])
print('Appended',x)

# increment with list comprehension
x[list(indx for indx in range (10) if indx%2 )] += 1
print ('Increment with list comprehension ', x)
x = x[list(indx for indx in range (10) if indx%2 )] + 1
print ('Increment with list comprehension 2', x)

# multiply
y = x*3
print('Multiply', y)
y= x**2
print('Square',y)
y = np.sin(x)
print('Sine',y)