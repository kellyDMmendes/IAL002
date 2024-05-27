# Solução do exercício 2 da lista de exercícios da Aula 7
A = []
valor = int(input('Digite valor: '))
while valor > 0:
    A.append(valor)
    valor = int(input('Digite valor: '))

print('\nExibição da Lista usando laço while')
i = 0
while i < len(A):
    print(A[i])
    i += 1

print('\nExibição da Lista usando o comando for')
for valor in A:
    print(valor)

print('\nExibição da Lista usando o comando for + range')
for i in range(len(A)): # este range gera a sequência de índices que começam em 0 e terminam no tamanho da lista A -1
    print(A[i])


print('\n\nFim do Programa')
