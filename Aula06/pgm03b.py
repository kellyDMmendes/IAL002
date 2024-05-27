# Solução do exercício 3 da lista de exercícios da Aula 6
# versão b

N = int(input('Digite N: '))
i = 0
X = float(input(f'Digite o elemento {i}: '))
guardaMenor = guardaMaior = X
while i < N-1:
    if X < guardaMenor:
        guardaMenor = X
    if X > guardaMaior:
        guardaMaior = X
    i += 1
    X = float(input(f'Digite o elemento {i}: '))

print(f'Menor valor = {guardaMenor}')
print(f'Maior valor = {guardaMaior}')

print('\n\nFim do Programa')
