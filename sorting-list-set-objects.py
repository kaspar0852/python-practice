
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
        self.salary = salary
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1 = Employee('Sau',21,60000)
e2 = Employee('hardik',21,40000)
e3 = Employee('guddu',21,35000)

employees = [e1,e2,e3]
#if we try to sort this without a key python will not know how to sort thme .

def e_sort(emp):
    return emp.name

s_employee = sorted(employees,key=e_sort)

#if we are familiar with lambda function something that small of a function can be written directly using lambda function
sal_employee = sorted(employees,key = lambda emp: emp.salary)

from operator import attrgetter
 
age_employee = sorted(employees,key = attrgetter('age'))

print(s_employee) #this returns all our emplyee based on their name
print(sal_employee)
print(age_employee)



