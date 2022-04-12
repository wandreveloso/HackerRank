# Este é um comentário e não faz parte da resolução do problema
# Este código foi retirado do GitHub https://github.com/wandreveloso
# Se você chegou a este código, entre no link e clique na estrela para apoiar esta iniciativa

"""
Desafio: https://www.hackerrank.com/challenges/simple-array-sum

O objetivo dessa questão é ensinar o uso do básico de funções com retorno e repetição.

Na questão anterior eu comentei a respeito de funções com retorno e aqui focarei na repetição.

Saliento que há inúmeras formas de resolver essa questão e optei por fazer da mais simples por questões didáticas.

A função recebe um array de inteiros, ou seja, um conjunto de números inteiros, e pede para retornar a soma deles.
Para isso, antes de percorrer os números eu crio uma variável chamada soma que se inicia com valor 0.

Para a repetição eu optei por usar um for i in ar, que significa que a variável i receberá o valor de cada um dos
elementos em ar (nosso array de inteiros), o que indica que todos os elementos do array serão percorridos. Por ser
uma tarefa repetitiva, utilizamos uma estrutura de repetição como for. Aí, dentro do for, dizemos que a variável soma
receberá o valor da soma antigo, acrescido pelo valor i, que é o valor agora do elemento do array. Esse tipo de
variável (soma) é chamada de variável acumuladora.
"""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    soma = 0  # Variável acumuladora
    for i in ar:  # O valor i vai receber todos os elementos de ar
        soma = soma + i
    return soma


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
