#!/bin/python3

import os


def sock_merchant(n, ar):
    seen = set()
    for i in ar:
        if i in seen:
            seen.remove(i)
        else:
            n -= 1
            seen.add(i)
    return n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sock_merchant(n, ar)
    fptr.write(str(result) + '\n')

fptr.close()
