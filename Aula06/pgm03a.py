# Solução do exercício 3 da lista de exercícios da Aula 6
# versão a

N = int(input('Digite N: '))
i = 0
while i < N:
    X = float(input(f'Digite o elemento {i}: '))
    if i == 0 or X < guardaMenor:
        guardaMenor = X
    if i == 0 or X > guardaMaior:
        guardaMaior = X
    i += 1

print(f'Menor valor = {guardaMenor}')
print(f'Maior valor = {guardaMaior}')

print('\n\nFim do Programa')
