# Solução do exercício 18 da lista de exercícios da Aula 9
'''from random import randint

def ExibeLista(lista):
    print(f'\nA lista gerada tem {len(lista)} elementos')
    print(' '*6, end='')
    for i in range(10):
        print(f'{i:5}', end='')
    i = 0
    print(f'\n{i:4}: ', end='')
    while i < len(lista):
        if i > 0 and i % 10 == 0:
            print(f'\n{i:4}: ', end='')
        print(f'{lista[i]:5}', end='')
        i += 1
    
N = int(input('Digite N: '))
while N <= 10:
    N = int(input('Digite N: '))
V = []
for _ in range(N):
    V.append(randint(1, 5000))

print('Antes da ordenação')
if N < 500:
    ExibeLista(V)

# Algoritmo Bubble Sort (Bolha)
HouveTroca = True
while HouveTroca:
    HouveTroca = False
    i = 0
    while i < N-1:
        if V[i] > V[i+1]:
            aux = V[i]
            V[i] = V[i+1]
            V[i+1] = aux
            HouveTroca = True
        i += 1
    
print('\n\nApós a ordenação')
if N < 500:
    ExibeLista(V)

print('\n\nFim do Programa')
'''
import os

# Obtendo o tamanho da tela
tamanho_da_tela = os.get_terminal_size().columns

# Imprimindo uma linha de tamanho variável
print('-' * tamanho_da_tela)
