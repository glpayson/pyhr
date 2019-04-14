#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    for x in range(len(c)):
        if x == len(c):
            continue
        elif x == len(c) - 1:
            jumps += 1
        elif c[x + 2] == 0:
            continue
        else:
            jumps += 1

    return jumps



foo = jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
bar = 11
