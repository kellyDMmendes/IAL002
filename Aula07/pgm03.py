# Enunciado
# Faça um programa que leia um inteiro Qtde.
# Em seguida gere uma lista com Qtde valores inteiros aleatórios entre 1 e 100
# Mostre essa lista na tela - todos os elementos de uma vez.
# Multiplique todos os valores da lista por um inteiro N fornecido (lido) e
#  mostre novamente

from random import randint

lista = []
Qtde = int(input('Digite Qtde: '))
for i in range(Qtde):
    lista.append(randint(1, 100))
print('\nLista gerada')
print(lista)

N = int(input('Digite N: '))
for i in range(Qtde):
    lista[i] = lista[i] * N
print(f'\nLista multiplicada por {N}')
print(lista)

print('\n\nFim do Programa')
