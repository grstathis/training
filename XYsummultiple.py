__author__ = 'stathis'
#Script to find the sum of all the multiples of 2 inputs below a range of numbers.
#Example:Find the sum of all the multiples of 3 or 5 below 1000.
#Euler Project Problem 1

import functools
import time


def multi_x_y(i, x, y):
    if (i % x == 0) | (i % y == 0):
        return i
    else:
        return 0


def sum_multi_x_y_list_compr(x, y, l_range):
    result = [multi_x_y(i,x,y) for i in range(l_range)]
    return sum(result)


def sum_multi_x_y_simple_for(x, y, l_range):
    result = 0
    for i in range(l_range):
        if (i % x == 0) | (i % y == 0):
            result += i
    return result


if __name__ == '__main__':

    x = 3
    y = 5
    l = 1000000

    ts = time.time()
    res = sum_multi_x_y_simple_for(x, y, l)
    te = time.time()
    print("Execution time using simple for loop", ts - te, "sum result:", res)

    ts = time.time()
    res = sum_multi_x_y_list_compr(x, y, l)
    te = time.time()
    print("Execution time using list comprehension", ts - te, "sum result:", res)