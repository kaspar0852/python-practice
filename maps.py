import collections 

dict1 = {'name':'Saugat','age':10}
dict2 = {'name2':'guddu','age2':15}

res = collections.ChainMap(dict1,dict2)

print(res.maps,'\n')
#output
''' [{'name': 'Saugat', 'age': 10}, {'name': 'guddu', 'age': 15}] ''' 

#ascessing the keys and values

print('Keys ={}'.format(list(res.keys())))
print('Values ={}'.format(list(res.values())))
#Output
''' Keys =['name', 'age']
Values =['Saugat', 10] '''

print('elements')
for key,val in res.items():
    print('{} = {}'.format(key,val))
    