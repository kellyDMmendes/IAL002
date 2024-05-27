# Solução do exercício 5 da lista de exercícios da Aula 6

X = int(input('Digite um valor: '))
while X != 0:
    if X % 2 == 0 and X % 3 == 0:
        print(f'  {X} é divisível por 2 e por 3')
    X = int(input('Digite um valor: '))

print('\n\nFim do Programa')
