#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    b_sum = 0
    l = len(q)

    for i in range(l):
        bribes = q[i] - i - 1
        if bribes > 2:
                print ("Too chaotic")
                return ("Too chaotic")

        elif bribes <= 0:
            if q[i] > 3:
                start_j = q[i] - 3
            else:
                start_j = 0   
            for j in range(start_j,i):
                if q[i] < q[j]:
                    b_sum += 1
            
    print (b_sum )
    return(b_sum )


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
