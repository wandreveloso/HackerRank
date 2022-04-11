# Este é um comentário e não faz parte da resolução do problema
# Este código foi retirado do GitHub https://github.com/wandreveloso
# Se você chegou a este código, entre no link e clique na estrela para apoiar esta iniciativa

"""
Desafio: https://www.hackerrank.com/challenges/py-if-else

O objetivo dessa questão é ensinar o uso dos comandos if, else e elif.

Repare que esse programa somente será executado até 1 print. Caso o número seja menor do que 1, não será impresso nada.
"""
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__': # Esta linha é usada para controle de escopo de execução, de forma que será executado somente o que está dentro deste if, mesmo que seja transformado o código em um arquivo interpretado
    n = int(input().strip()) # Esta linha pega o que o usuário irá digitar (comando input), pegar até antes de um espaço ou enter que tiver (strip) e transformar a entrada para um número inteiro e guardar na variável n
    if n % 2 == 1: # Aqui é usado o comando % para pegar o resto da divisão e, nesta linha, verifica se o número n é ímpar
        print("Weird") #impresso se número for ímpar
    # A partir daqui, somente será executado caso n seja par
    elif n>=2 and n<=5: # Ao invés de usar else if, como em outras linguagens, o Python tem o elif que é a junção do else e de um novo if
        print("Not Weird") # Impresso se número for par e entre 2 e 5, intervalo fechado
    elif n>=6 and n<=20:
        print("Weird") # Impresso se número for par e entre 6 e 20, intervalo fechado
    elif n>20:
        print("Not Weird") # Impresso se número for par e maior que 20

