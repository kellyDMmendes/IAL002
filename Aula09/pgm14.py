# Solução do exercício 14 da lista de exercícios da Aula 9
from random import randint

A = []
for i in range(10):
    X = randint(100, 999)
    A.append(X)
print('Lista A gerada')
print(A)

B = []
for i in range(10):
    X = randint(100, 999)
    B.append(X)
print('Lista B gerada')
print(B)

# R = A + B    # em Python é possível fazer desta forma.
# Mas queremos fazer de um que utilize algum tipo de lógica (algoritmo)
R = []
i = 0
while i < 10:       # este laço acrescenta os elementos de A em R
    R.append(A[i])
    i += 1
i = 0
while i < 10:       # este laço acrescenta os elementos de B em R
    R.append(B[i])
    i += 1
print('Junção de A com B')
print(R)

print('\n\nFim do Programa')
