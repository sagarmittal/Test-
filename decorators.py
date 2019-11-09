import time


# a decorator is a function which returns a function and takes in a function and performs some added functionalities


# this is a wrapper function and it takes in a function as an argument
def time_it(func):
    # wrapper is a first class function
    def wrapper(*args, **kwargs):
        # this is an inner function
        start = time.time()
        result = func(*args, **kwargs)
        # func is an free variable i.e.,
        # we don't have access to it even though we didn't call it
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + 'mil seconds')
        return result

    # we dont need to put a closure over here
    return wrapper


# its same if we use :
# some_variable = time_it(calc_square)
@time_it
def calc_square(numbers):
    # start = time.time()
    result = []
    for number in numbers:
        result.append(number * number)
    # end = time.time()
    # print('calc_square took ' + str((end-start)*1000) + 'mil-sec')
    return result


@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number ** 3)
    return result


# array = range(1, 100000)
# out_square = calc_square(array)
# out_cube = calc_cube(array)


# //////////////////////////////////////////////////////////
# USING CLASS AS A DECORATOR

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'Call method was executed in decorator class before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)


# TO USE MULTIPLE DECORATORS
# WE MUST WRAP THE DECORATOR FUNCTION -> TO PRESERVE ITS ORIGINAL INFORMATION
from functools import wraps


# used to log
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    # we are running decorator inside the decorator
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


# used to calculate the time taken by the function
def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = orig_func(*args, **kwargs)
        end = time.time()
        print(f'{orig_func.__name__} ran in: {end - start} seconds')
        return result

    return wrapper


@decorator_class
def display():
    print('display function ran')


@my_logger
@my_timer
def display_info(name, age):
    import time
    time.sleep(1)  # we gave it a lag of a second
    print("the name is {'name'} and age is {'age'} ")


display_info('sagar', age=20)
