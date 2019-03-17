__author__ = 'stathis'
import math
import copy
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):

    x.sort()
    min_antenna = math.ceil((x[len(x) - 1] - x[0])/float(2*k))
    for i in range(len(x)):
        l = x[i] - k
        r = x[i] + k
        if r >= x[0] >= l:
            antenna_num = 1
            for j in range(i, len(x)):
                if r < x[j]:
                    antenna_num += 1
                    r = x[j] + k
                    l = x[j] - k

            if antenna_num < min_antenna:
                min_antenna = antenna_num
        else: break

    return antenna_num


def funGame(a, b):

    moves = range(len(a))
    a_win = [False]*len(a)
    b_win = [False]*len(a)
    tie = [False]*len(a)
    if a == b and len((set(a))) > 1:
        return ("First")
    elif a == b and len((set(a))) == 1:
        return ("Tie")


    for start in moves:
        a_score = a[start]
        b_score = 0
        a_new = dict([(key,value) for key,value in enumerate(a)])
        b_new = dict([(key,value) for key,value in enumerate(b)])
        del a_new[start]
        del b_new[start]

        if len(b_new) != 0:
            i = max(b_new, key=b_new.get)
            b_score += b_new[i]
            del a_new[i]
            del b_new[i]

        while len(a_new) != 0:
            i = i = max(a_new, key=a_new.get)
            a_score += a_new[i]
            del a_new[i]
            del b_new[i]

            if len(b_new) != 0:
                i = max(b_new, key=b_new.get)
                b_score += b_new[i]
                del a_new[i]
                del b_new[i]

        if a_score > b_score:
            a_win[start] = True
        elif a_score < b_score:
            b_win[start] = True
        else:
            tie[start] = True

    if any(a_win):
        return ("First")
    elif all(b_win):
        return ("Second")
    elif any(tie):
        return ("Tie")



if __name__ == '__main__':

    n = 5

    k = 2
    x = [1,2,3,4,5]
    x = [7, 2, 4, 6, 5, 9, 12, 11]

    result = hackerlandRadioTransmitters(x, k)

    #print(result)

    a = [1,1,2,2]
    b = [1,1,2,2]

    res = funGame(a, b)
    print(res)