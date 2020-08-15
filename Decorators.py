import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, ' took : ', str((end - start) * 1000) + "mil sec")
        return result

    return wrapper


@time_it
def calc_square(number):
    print("calculate square of numbers")
    result = []
    for n in number:
        result.append(n * n)
    return result


@time_it
def calc_cube(number):
    print("calculate cube of numbers")
    result = []
    for n in number:
        result.append(n * n * n)
    return result


array = range(1, 100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
