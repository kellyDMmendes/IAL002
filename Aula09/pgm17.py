# Solução do exercício 17 da lista de exercícios da Aula 9

def EstaNaLista(valor, lista):
    """procura valor em lista, retorna True se encontrar, caso contrário retorna False"""
    i = 0
    while i < len(lista):
        if valor == lista[i]:
            return True
        i += 1
    return False


nA = int(input('Tamanho de A: '))
A = []
i = 0
while i < nA:
    X = int(input(f'  elemento {i}: '))
    if not EstaNaLista(X, A):
        A.append(X)
        i += 1
    else:
        print('  ...repetido')
print('Lista A lida')
print(A)

nB = int(input('\nTamanho de B: '))
B = []
i = 0
while i < nB:
    X = int(input(f'  elemento {i}: '))
    if not EstaNaLista(X, B):
        B.append(X)
        i += 1
    else:
        print('  ...repetido')
print('Lista B lida')
print(B)

R = []
i = 0
while i < nA:       # este laço acrescenta os elementos de A em R
    R.append(A[i])
    i += 1
i = 0
contRep = 0
while i < nB:       # este laço acrescenta os elementos de B em R
    if not EstaNaLista(B[i], R):
        R.append(B[i])
    else:
        contRep += 1
    i += 1
print(f'\nJunção de A com B tem {nA + nB - contRep} elementos')
print(R)

print('\n\nFim do Programa')
