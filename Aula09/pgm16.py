# Solução do exercício 16 da lista de exercícios da Aula 9

def EstaNaLista(valor, lista):
    """procura valor em lista, retorna True se encontrar, caso contrário retorna False"""
    i = 0
    while i < len(lista):
        if valor == lista[i]:
            return True
        i += 1
    return False


L = []
N = int(input('Digite o tamanho N: '))
i = 0
while i < N:
    X = int(input(f'  elemento {i}: '))
    if not EstaNaLista(X, L): 
        L.append(X)
        i += 1
    else:
        print('    ...valor inválido. Repetido')

print('Lista final')
print(L)
print('\n\nFim do Programa')
