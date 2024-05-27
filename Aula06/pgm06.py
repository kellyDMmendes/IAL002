# Solução do exercício 6 da lista de exercícios da Aula 6
N = int(input('Digite N: '))
while N < 100:
    print(f'{N} é muito pequeno. Deve ser no mínimo 100')
    N = int(input('Digite N: '))
soma = 0
a = 2
while a <= N:
    soma += a
    a += 2
    
print(f'Soma dos pares até {N} = {soma}')

print('\n\nFim do Programa')
