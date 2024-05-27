# Solução do exercício 2 da lista de exercícios da Aula 9
A = []
i = 0
while i < 10:
    valor = int(input('Digite valor: '))
    A.append(valor)
    i += 1

print('\nExibição da Lista em ordem inversa, usando while e nenhum recurso especial de Python')
i = 9 # o valor inicial é 9 porque a lista tem 10 elementos
while i >= 0:
    print(A[i])
    i -= 1

print('\nExibição da Lista usando o comando for em conjunto com o método .reverse da classe list')
A.reverse()
for valor in A:
    print(valor)


print('\n\nFim do Programa')
