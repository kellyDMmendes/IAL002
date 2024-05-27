"""Exibia na tela os N primeiros termos de uma PA
   com primeiro termo P e Razão R"""

N = int(input('Digite N: '))
P = int(input('Digite P: '))
R = int(input('Digite R: '))

cont = 0
while cont < N:
    print(P)
    P = P + R
    cont += 1

print('\n\nFim do Programa')
