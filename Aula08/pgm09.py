# Solução do exercício 9 da lista de exercícios da Aula 9
from random import randint

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
    

# programa principal
N = int(input('Digite N maior que 0: '))
while N < 1:
    print(f'  {N} é inválido')
    N = int(input('Digite N maior que 0: '))

A = []
for i in range(N):
    A.append(randint(0, 1000))
ExibeLista(A)

X = int(input('\n\nDigite X: '))
while X >= 0:
    if X in A:
        print(f'  {X} está na lista')
    else:
        print(f'  {X} não está na lista')
    X = int(input('Digite X: '))

    
print('\n\nFim do Programa')







