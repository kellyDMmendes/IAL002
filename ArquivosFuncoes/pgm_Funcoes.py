# Este programa exemplifica o uso de funções

from random import randint

def Soma(a, b):
    '''Esta função soma a com b e retorna esse resultado'''
    r = a + b
    return r

def Operacoes(a, b):
    '''retorna soma, subtração, multiplicação e divisão entre a e b '''
    return a+b, a-b, a*b, a/b

v1 = int(input(' valor 1 >> '))
v2 = int(input(' valor 2 >> '))
resultado = Soma(v1, v2)
print(f'Soma de {v1} com {v2} = {resultado}')

ops = Operacoes(v1, v2)
print('Resultado das Operacoes:')
print(f'  soma          = {ops[0]}')
print(f'  subtração     = {ops[1]}')
print(f'  multiplicação = {ops[2]}')
print(f'  divisão       = {ops[3]}')

print('\n\nFim do Programa')


