# Este é um comentário e não faz parte da resolução do problema
# Este código foi retirado do GitHub https://github.com/wandreveloso
# Se você chegou a este código, entre no link e clique na estrela para apoiar esta iniciativa

"""
Desafio: https://www.hackerrank.com/challenges/staircase

O objetivo dessa questão é ensinar
"""
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    temp = 1
    for i in range(n):
        car = ''
        for k in range(n - temp):
            car = ''.join([car, ' '])
        for l in range(temp):
            car = ''.join([car, '#'])
        temp += 1
        print(car)


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
