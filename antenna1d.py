#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_left


# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):

    antenna_pos = [0]*len(x)
    antenna = 1
    rrange = x[0] + k
    lrange  = x[0] - k
    house_cov_right = set([ j for j in range(len(x)) if (x[j] <= rrange) and (x[j] >= x[0])])
    house_cov_left  = set([ j for j in range(len(x)) if (x[j] >= lrange) and (x[j] <= x[0])])
    print(house_cov_left)
    print(house_cov_right)
    for i in range(1, len(x)):
        new_rrange = x[i] + k
        new_lrange = x[i] - k
        house_cov_idx_new = set([j for j in range(len(x)) if (x[j] <= new_rrange) and (x[j] >= new_lrange)])
        if house_cov_idx <= house_cov_idx_new:
            print("covered, no new antenna needed")
            house_cov_idx = house_cov_idx_new
        else:
            house_cov_new = house_cov_idx_new.intersection(house_cov_idx)

            antenna = antenna + 1



    return antenna




def minimumLoss(price):

    buy_price = price[0]
    sell_opt_org = price[1:]
    sell_opt_org.sort()
    j = bisect_left(sell_opt_org, buy_price)
    sell_opt = sell_opt_org[:j]
    loss = buy_price - sell_opt[-1]

    for i in range(1, len(price)):
        buy_price = price[i]
        sell_opt_org.remove(buy_price)
        j = bisect_left(sell_opt_org, buy_price)
        sell_opt = sell_opt_org[:j]
        if sell_opt:
            loss_new = buy_price - sell_opt[-1]
            if loss_new < loss:
                loss = loss_new

    return loss



if __name__ == '__main__':


    x = [20,7 ,8, 2, 5]
    #x.sort()
    res = minimumLoss(x)
    print(res)
    #result = hackerlandRadioTransmitters(x, k)
    #print(result)

