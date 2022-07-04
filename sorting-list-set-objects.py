
#sorting a lisyt 
li = [9,8,8,2,7,6,4,5]

""" li = sorted(li) """
li.sort()

print(li)

this_li = [-6,-5,2,1,3]
s_this_li = sorted(this_li,key=abs)
print(s_this_li)

#sorting tuple 

tup = (9,8,8,2,7,6,4,5)
""" tup.sort() """ #this gives us an error
s_tup = sorted(tup)
sr_tup = sorted(tup,reverse = True)
print(s_tup)
print(sr_tup)
#the sorted method gives us more flexibility than the sort method

#sorting dictionary

di = {'name':'Saugat','age':21,'job':'student'}
s_di = sorted(di) #what this will do by default is that it will sort the keys 
#the output will me ['age','job','name']
print(s_di) 


class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salry = salary
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1 = Employee('Sau',21,30000)
e2 = Employee('hardik',21,40000)
e3 = Employee('guddu',21,35000)

employees = [e1,e2,e3]



