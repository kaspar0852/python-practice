#List

courses = ['History','Maths','Python','Physics']
courses2 = ['Java','DotNet','C#']

nums = [1,5,6,3,2,7]
''' print(courses) '''

#see how many value in our list

''' print(len(courses)) '''
''' 
print(courses[0]) '''

''' print(courses[0:2]) '''

''' here 0 is starting point and 2 is stoping point '''

''' print(courses[:2]) '''
'''  this also gives the same value as abouve '''

''' courses.append('Art') '''

''' print(courses) '''

''' now if we want to insert item in a specific location then we can use
insert method here the first argument is location and 2nd is the value''' 

''' courses.insert(0,'Apple')

print(courses)
 '''
''' another way of adding item to our list is by using the extend method
   we want to use extend when we have multiple value we want to insert in out list'''
   
''' courses.insert(0,courses2)  we can add like this also but see the output for difference while using extend'''


''' courses.extend(courses2)

print(courses) '''

#remove values from list

''' courses.remove('Maths')

print(courses) '''

#passing nothing into pop method will delete the last item from the list
#one thing abt pop is it returns the value it poped out  
''' popped = courses.pop()  
print(popped)
print(courses) '''

#sorting out list
#reversing the list courses
''' courses.reverse()
print(courses) '''

#sorting

courses.sort()
print(courses)

''' nums.sort() ''' #this sorts in ascending order and also the above sort
nums.sort(reverse = True)
print(nums)

#what if we wanted sorted version of a list without disturbing or altering the orginal list,
#we can use sorted method

sorted_courses = sorted(courses)
print(courses)
print(sorted_courses)

#if i wannt min value of our nums list

print(min(nums))

#if i want max

print(max(nums))

#if i want sum of that entire numbers then 

print(sum(nums))


#this retrurns true or false
print('History' in courses)

#convert the list into string seperated by some values
#here the comma  seperates each value from the courses list 
course_str = ' , '.join(courses)
print(course_str)

#turn string back into a list
#this splits all the values from space , space and creates a list
new_list = course_str.split(' , ')
print(new_list)






#Tuples

tuple_1 = ('History','Maths','Python','Physics')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)
#we cannot perform the below operation becaue tuples are immutable
''' tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2) '''






#Sets
# -> unordered and doesnot contain duplicate values

cs_course = {'History','Maths','Python','Physics','Maths'}
art_course = {'Design','Maths','Art','Physics'}


print(cs_course)
# -> it is also used to test either a value is a part of a set which is also called membership test
print('Math' in cs_course)

# -> another this sets can do is determine what values they share or not share  with another set
# to do this we can use intersection method
#this shows what values they share ie because of intersection method
print(cs_course.intersection(art_course))

#if i want to see what courses are in cs_courses but not in art_courses then we use difference method

print(cs_course.difference(art_course))

#if i want to combine these 2 sets and combine all the items then we can use union method

print(cs_course.union(art_course))

#create empty list,tuples and sets
#empty list
empty_list = []
empty_list = list()

#empty tuple
empty_tuple = ()
empty_tuple = tuple()

#empty sets

empty_sets = {} #this is not right it will create a empty dictionary
empty_sets = list()








