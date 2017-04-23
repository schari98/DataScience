import pandas as pd
import csv
import numpy as np


print("DataFrame from a list of dicts")
listdict1 = [ {'name':'Joe','age':30,'weight':130,'city':'Atlanta'},
              {'name': 'John', 'age': 23, 'weight': 140, 'city': 'NewYork'},
              {'name': 'Mike', 'age': 40, 'weight': 170, 'city': 'Seattle'}]
df1 = pd.DataFrame(listdict1)


print(df1)

print("DataFrame from a list of dicts with one of the fields as index")
listofnames = [ x['name'] for x in listdict1]
for x in listdict1:
    x.pop('name')
print(listofnames)
print (listdict1)
df2 = pd.DataFrame(listdict1,index=listofnames)
print(df2)

print("\n Use .loc to index ")
print(df2.loc['Joe'])
'''
mpegdict=[]
filehandle = open('c:\\arris\projects\Data Science\mpg.csv','rt')
mpeg = csv.DictReader(filehandle)
for row in mpeg:
    mpegdict.append(row)
df2 = pd.DataFrame(mpegdict)
print(df2)
filehandle.close()
'''

dfcsv = pd.read_csv('c:\\arris\projects\Data Science\mpg.csv',)
print(dfcsv.head(5))
print("Average mileage {}".format(np.average(dfcsv.loc[:,'mpg'])))
