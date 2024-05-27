# Solução do exercício 18 da lista de exercícios da Aula 9

L = []
X = int(input('Digite X: '))
while X > 0:
    i = 0
    while i < len(L) and X > L[i]:
        i += 1
    L.insert(i, X)
    print(L)
    
    X = int(input('\nDigite X: '))

print('\n\nFim do Programa')
