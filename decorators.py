import time


# this is a wrapper function and it takes in a function as an argument
def time_it(func):
    # wrapper is a first class function
    def wrapper(*args, **kwargs):
        # this is an inner function
        start = time.time()
        result = func(*args, **kwargs)
        # func is an inner function i.e.,
        # we don't have access to it even though we didn't call it
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + 'mil seconds')
        return result
    # we dont need to put a closure over here
    return wrapper


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


array = range(1, 100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
