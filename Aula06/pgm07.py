# Solução do exercício 7 da lista de exercícios da Aula 6

soma = qtde = 0
A = int(input('Digite um valor: '))
guardaMenor = guardaMaior = A
while A > 0:
    soma += A
    qtde += 1
    if A < guardaMenor:
        guardaMenor = A
    if A > guardaMaior:
        guardaMaior = A
    A = int(input('Digite um valor: '))

if qtde > 0:
    print('Resultados')
    print(f'Menor valor = {guardaMenor}')
    print(f'Maior valor = {guardaMaior}')    
    print(f'Soma  = {soma}')
    print(f'Qtde  = {qtde}')
    print(f'Média = {soma / qtde}')
else:
    print('Não foram digitados valores válidos')
    

print('\n\nFim do Programa')
