#Normal method

''' def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_numbers = square_numbers([1,2,3,4,5])

print(my_numbers) ''' #the output will be [1,4,9,16,25]



#currently our square_numbers function is returning a list now how would we convert this to be a generator

''' def square_numbers(nums):

    for i in nums:
        yield (i*i)                #this yield makes this generator
   
my_numbers = square_numbers([1,2,3,4,5]) '''

#using list comprehension to do this above work

''' my_numbers = [x*x for x in [1,2,3,4,5]] '''

#now we can make this list comprehension to generator as 

my_numbers = (x*x for x in [1,2,3,4,5])

''' print(my_numbers) ''' #the output will not be a list of numbers because-
#-generators dont hold entire result in the memory, it yeilds one result over time
#this is waiting for us to ask for a new result,so it hasnt computed anything yet
#so we need to do something like this using next:
''' print (next(my_numbers))
print (next(my_numbers))
print (next(my_numbers))
print (next(my_numbers))
print (next(my_numbers)) '''
''' this will give result as 1 4 9 16 25
 '''
''' but instead of doing one at time lets loop the output '''
for nums in my_numbers:
    print (list(nums))

#as we pass the generator output to the list we do loose its advanage of generators  mainly performance
#advantage over list is :This is much more readable than the normal method shown at top