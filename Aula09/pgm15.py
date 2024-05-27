# Solução do exercício 15 da lista de exercícios da Aula 9

nA = int(input('Tamanho de A: '))
A = []
for i in range(nA):
    X = int(input(f'  elemento {i}: '))
    A.append(X)
print('Lista A lida')
print(A)

nB = int(input('\nTamanho de B: '))
B = []
for i in range(nB):
    X = int(input(f'  elemento {i}: '))
    B.append(X)
print('Lista B lida')
print(B)

# R = A + B    # em Python é possível fazer desta forma.
# Mas queremos fazer de um que utilize algum tipo de lógica (algoritmo)
R = []
i = 0
while i < nA:       # este laço acrescenta os elementos de A em R
    R.append(A[i])
    i += 1
i = 0
while i < nB:       # este laço acrescenta os elementos de B em R
    R.append(B[i])
    i += 1
print(f'\nJunção de A com B tem {nA + nB} elementos')
print(R)

print('\n\nFim do Programa')
