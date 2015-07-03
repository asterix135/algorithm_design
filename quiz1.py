import math
import matplotlib.pyplot as pyplot


def gen_vals(list, func):
    temp_list = []
    for num in list:
        temp_list.append(func(num))
    return temp_list

def gen_ten_to_nth(val):
    '''return ten to the nth'''
    return 10**val

def gen_n_to1point5 (val):
    '''return n to the 1.5 power'''
    return val**1.5

def gen_two_to_sqrt_log_n (val):
    '''return 2 to the square root of log2 of n'''
    return math.sqrt(math.log2(val))

def gen_n_to_5thirds (val):
    '''return n to the 5/3 power'''
    return val**(5/3)

def generate_chart(value_range):

    x_values = gen_vals(value_range, float)
    square_roots = gen_vals(value_range, math.sqrt)
    # ten_to_n = gen_vals(value_range, gen_ten_to_nth)
    n_to_one_point_five = gen_vals(value_range, gen_n_to1point5)
    two_to_sqrt = gen_vals(value_range, gen_two_to_sqrt_log_n)
    n_to_five_thirds = gen_vals(value_range, gen_n_to_5thirds)

    pyplot.plot(x_values, square_roots, label='square roots')
    # pyplot.plot(x_values, ten_to_n, label = 'ten to the nth')
    pyplot.plot(x_values, n_to_one_point_five, label = 'n to the 1.5')
    pyplot.plot(x_values, two_to_sqrt, label = 'two to the sqrt(lot of n)')
    pyplot.plot(x_values, n_to_five_thirds, label = 'n to the 5/3')
    pyplot.legend(loc='upper left')
    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.show()

number_list = range(1,301)
generate_chart(number_list)

