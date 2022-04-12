# Este é um comentário e não faz parte da resolução do problema
# Este código foi retirado do GitHub https://github.com/wandreveloso
# Se você chegou a este código, entre no link e clique na estrela para apoiar esta iniciativa

"""
Desafio: https://www.hackerrank.com/challenges/diagonal-difference

O objetivo dessa questão é ensinar
"""
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    tam = len(arr)
    prin = 0
    sec = 0
    for i in range(tam):
        prin += arr[i][i]
        sec += arr[i][tam - i - 1]
    if prin > sec:
        return prin - sec
    else:
        return sec - prin


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
