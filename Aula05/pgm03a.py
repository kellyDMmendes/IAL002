"""Escreva um programa que permaneça em laço lendo números inteiros
   totalizando-os e contando-os.
   O laço termina quando for digitado o valor zero (0).
   Ao final, mostre o total, a quantidade e a média dos valores. """

soma = qtde = 0
X = 1
while X != 0:
    X = int(input('Digite X: '))
    soma = soma + X
    qtde += 1

qtde -= 1
if qtde > 0:
    print('\nResultados')
    print(f'  Soma  = {soma}')
    print(f'  Qtde  = {qtde}')
    print(f'  Média = {soma/qtde}')
else:
    print('\nNão foram fornecidos dados')

print('\n\nFim do Programa')
