#A decorator is a function that takes another function as an argument adds some kind of functionality-
#-and returns another function...all of these without altering the source code of the oorginal function-
#-that we passed in 

""" def decorator_function(message):
    def wrapper_function():
        print(message)
    return wrapper_function

hi_func = decorator_function('HI')
bye_func = decorator_function('Bye')

hi_func()
bye_func() """

#here this function returns a wrapper function which is waiting to be executed and when it is excuted the-
#-original function will be executed
""" Decorators helps to add functionality to our existing function by adding the functionality inside our wrapper """

""" def decorator_function(orginal_function):
    def wrapper_function():
        return orginal_function()
    return wrapper_function


def display():
    print('I am DON')

decorated_display = decorator_function(display)

decorated_display() """
#instead of writing these 2 lines of code we can just add @decorator_funcion on top of our display method which will mean the same as these-
#-2 line and then call display .Lets demonstrate this

def decorator_function(orginal_function):
    def wrapper_function(*args,**kwargs):
        return orginal_function(*args,**kwargs)
    return wrapper_function

#with the help of args and kwargs we can pass any number of arguments and keyword arguments

@decorator_function
def display_info(name,age):
    print('display info ran with arguments ({},{})'.format(name,age))   

@decorator_function
def display():
    print('I am DON')

display()
display_info('saugat',21)

