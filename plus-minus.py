# Este é um comentário e não faz parte da resolução do problema
# Este código foi retirado do GitHub https://github.com/wandreveloso
# Se você chegou a este código, entre no link e clique na estrela para apoiar esta iniciativa

"""
Desafio: https://www.hackerrank.com/challenges/plus-minus

O objetivo dessa questão é ensinar
"""
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    zero = par = impar = 0
    for i in arr:
        if i == 0:
            zero += 1
        elif i >= 0:
            par += 1
        else:
            impar += 1
    soma = par + impar + zero
    rpar = round(par / soma, 6)
    rimpar = round(impar / soma, 6)
    rzero = round(zero / soma, 6)
    print(rpar)
    print(rimpar)
    print(rzero)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
