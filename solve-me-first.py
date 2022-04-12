# Este é um comentário e não faz parte da resolução do problema
# Este código foi retirado do GitHub https://github.com/wandreveloso
# Se você chegou a este código, entre no link e clique na estrela para apoiar esta iniciativa

"""
Desafio: https://www.hackerrank.com/challenges/solve-me-first

O objetivo dessa questão é ensinar o uso do básico de funções com retorno.

Perceba que a função é definida, em Python, com o comando def, seguido do nome da mesma e os parâmetros entre parênteses

Os parâmetros são os valores que são passados para a função com o objetivo de ela realizar operações internas com os
valores recebidos por parâmetros (ou também chamados de argumentos).

A função solveMeFirst executa somente 1 comando, que é retornar a soma de duas variáveis. Esse retorno significa que,
onde a função for chamada, após a execução, o controle do código passará para os comandos da função e, após o término
da mesma, o resultado da função (do comando return) substituirá a chamada da função.

Se, por exemplo, for digitado para num1 o valor 5 e o num2 tiver valor 8, então, quando a função for executada,
o cálculo será processado e o valor 13 irá para a variável res
"""


def solveMeFirst(a, b):
    # Hint: Type return a+b below
    return a + b


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1, num2)
print(res)
