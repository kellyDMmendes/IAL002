"""Solução do problema de cálculo das raízes de uma
   equação de segundo grau"""
from math import sqrt # necessária a importação da função sqrt do módulo math

A = float(input('Digite A: ')) 
B = float(input('Digite B: '))
C = float(input('Digite C: '))

delta = B ** 2 - 4 * A * C
if delta > 0:
    X1 = (-B - sqrt(delta)) / (2 * A)
    X2 = (-B + sqrt(delta)) / (2 * A)
    print('Esta equação tem duas raizes')
    print(f'  X1 = {X1}')
    print(f'  X2 = {X2}')
elif delta == 0:
    X1 = -B / (2 * A)
    print('Esta equação tem uma raiz')
    print(f'  X1 = X2 = {X1}')
else:
    print('Esta equação não tem raizes reais')      

print('\n\nFim do Programa')

