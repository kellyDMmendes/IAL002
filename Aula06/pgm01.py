# Solução do exercício 1 da lista de exercícios da Aula 6
N = int(input('Digite N: '))

print('Solução com f-string')
cont = 1
while cont <= 10:
    print(f'{N:3} x {cont:3} = {N*cont:3}')
    cont += 1

print('\nSolução com string formatado')
cont = 1
while cont <= 10:
    print('{:3} x {:3} = {:3}'.format(N, cont, N*cont))
    cont += 1

print('\n\nFim do Programa')
