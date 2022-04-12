# Este é um comentário e não faz parte da resolução do problema
# Este código foi retirado do GitHub https://github.com/wandreveloso
# Se você chegou a este código, entre no link e clique na estrela para apoiar esta iniciativa

"""
Desafio: https://www.hackerrank.com/challenges/compare-the-triplets

O objetivo dessa questão é ensinar a usar funções, a retornar valores por funções, a usar repetições e condicionais.

Primeiro a função compareTriplets recebe 2 variáveis, sendo a para as notas que Alice recebeu e b para as de Bob. O
program solicita que cada uma das notas de Alice e Bob sejam comparadas e, por fim, retorne a quantidade de vezes que
Alice teve nota maior do que o Bob e quantas vezes o Bob teve nota maior que Alice (cada um em uma variável distinta).

Para isso, 2 arrays (a e b) são enviados como parâmetros para a função que se inicia atribuindo a quantidade de vezes
que Alice e Bob possuem nota maior do que o outro como 0. Depois, como já sabemos que terão somente 3 notas,
faço um for que vai atribuir à variável indice os valores de range(0,3), que são 0, 1 e 2 (lembrando que a função
range tem como primeiro parâmetro o número inicial e como segundo o valor final com intervalo fechado). Agora é
basicamente realizar a comparação dos valores de a e b individualmente, atribuindo +1 para Alice ou Bob.

Vale salientar que o Python trabalha com arrays tendo o primeiro elemento o elemento de índice 0.
"""
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice = 0  # Variável acumuladora
    bob = 0  # Variável acumuladora
    for indice in range(0, 3):  # indice vai receber os valores 0, 1 e 2
        if a[indice] > b[indice]:  # Se a nota de a for maior que de b
            alice += 1
        elif b[indice] > a[indice]:  # Se a nota de b for maior que de a
            bob += 1
    #  Somente vai sair do for quando percorrer as 3 notas de a e b
    return [alice, bob]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
