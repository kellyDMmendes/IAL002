# Solução do exercício 3 da lista de exercícios da Aula 9
N = int(input('Digite N entre 0 e 50: '))
while N < 0 or N > 50:
    print(f'  {N} é inválido')
    N = int(input('Digite N entre 0 e 50: '))

A = []
i = 0
while i < N:
    valor = float(input('Digite um valor real: '))
    A.append(valor)
    i += 1

print('\nExibição da Lista lida')
for valor in A:
    print(valor)


print('\n\nFim do Programa')
