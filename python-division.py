# Este é um comentário e não faz parte da resolução do problema
# Este código foi retirado do GitHub https://github.com/wandreveloso
# Se você chegou a este código, entre no link e clique na estrela para apoiar esta iniciativa

"""
Desafio: https://www.hackerrank.com/challenges/python-division

O objetivo dessa questão é ensinar a divisão entre valores.

Praticamente existem 3 formas diferentes de divisão: parte inteira da divisão, divisão convencional e resto da divisão.

Para parte inteira da divisão, usamos o símbolo // (duas barras) e retorna, para 7//3, o número inteiro 2 (ele trunca
o resultado da divisão convencional).

Na divisão convencional, usamos o símbolo / (uma única barra) e retorna, para 7/3, o número real 2.3333333333333335.

Por fim, para resto da divisão usamos o símbolo % (porcentagem) e retorna, para 7%3, o número inteiro 1, pois,
é uma divisão inexata e "sobra" 1. """
if __name__ == '__main__':
    a = int(input())  # Pega a entrada do usuário, converte para inteiro e guarda na variável a
    b = int(input())
    print(a // b)  # Parte inteira da divisão
    print(a / b)  # Divisão exata
