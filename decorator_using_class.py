class Decorator_class(object):
    def __init__(self,orginal_function):
        self.orginal_function = orginal_function


    #here this call method is just like the wrapper function which i implemented in the decorators file
    def __call__(self,*args,**kwargs):
        return self.orginal_function(*args,**kwargs)


@Decorator_class
def display_info(name,age):
    print('display info ran with arguments ({},{})'.format(name,age))   

@Decorator_class
def display():
    print('I am DON')

display()
display_info('saugat',21)

#here this will gvie the same result as the decorator file 
#here we used the class method