student = {'name':'John','age':25,'courses':['Math','CompSci']}

print(student)


print(student['name'])

print(student['courses'])

print(student.get('name'))

#new entry to dictionary

student['phone'] = '55555-555'

print(student)

student['name'] = 'Ram'
#the name gets updated to Ram

print(student)

#we can also update values using update method 
#this is useful if we want to update multiple values at a time

student.update({'name':'sau','age':21})

print(student)

#delete specific key and values

del student['age']

print(student)

#we can also use pop method to remove 
student['age'] = 10

age = student.pop('age')

print(student)
print(age)
 
 
 #iterating through a dictionary
print('\n')

#see how many keys we have in out dictionary

print(len(student))

#printing all the keys 

print(student.keys())

print(student.values())

print(student.items())

#this only loops through the keys 
for key in student:
    print(key)

#so if we want to loop thourgh both keys and values then we need that items method we just used above

for key,value in student.items():
    print(key,value)

