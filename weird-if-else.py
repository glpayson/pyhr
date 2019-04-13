#!/bin/python3

n = int(input())

if (n % 2 == 0) and (n == 2 or n == 4 or n > 20):
    print("Not Weird")
else:
    print("Weird")
