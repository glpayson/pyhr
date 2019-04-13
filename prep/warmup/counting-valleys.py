#!/bin/python3

import os

def counting_valleys(n, s):
    elevation = 0

    for c in s:
        elevation = elevation + 1 if c == 'U' else elevation - 1
        n = n if elevation == 0 and c == 'U' else n - 1

    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = counting_valleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
