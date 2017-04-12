
import csv
import sys
import collections

'''
Different variants of reading a csv file
'''

'''
Using the list(DictReader) as in coursera
'''
print ('Option 1')
#with open('c:\\arris\projects\Data Science\mpg.csv') as csvfile:
filehandle = open('c:\\arris\projects\Data Science\mpg.csv', 'rt')
mpeg = list(csv.DictReader(filehandle))
print(type(mpeg))
mpgover18=0
for row in mpeg:
    if float(row['mpg']) >= 18:
       mpgover18+=1
print ('mpgover18', mpgover18)
print ("keys", mpeg[0].keys())
print (mpeg[0])
filehandle.close()


'''
Create an empty list and add dictionaries to it
'''
print ('Option 2')
mpegdict=[]
filehandle = open('c:\\arris\projects\Data Science\mpg.csv','rt')
mpeg = csv.DictReader(filehandle)
for row in mpeg:
    mpegdict.append(row)
print(type(mpeg))
mpgover18=0
for row in mpegdict:
    if float(row['mpg']) >= 18:
        mpgover18+=1
print ('mpgover18', mpgover18)
print (mpegdict[1])
filehandle.close()



mydict = [{'fname': 'John','lname':'Doe','city': "Atlanta"},
            {'fname': 'Jane','lname':'Doe','city':'Macon'}]
print (mydict)
print (mydict[0].keys())
print (mydict[0].values())
for x in mydict:
    print(x['city'])


print(list(d['fname'] for d in mydict))

mylist = [ i*j for i in range(10) for j in range(10) if(i==j+1)]
print (mylist)