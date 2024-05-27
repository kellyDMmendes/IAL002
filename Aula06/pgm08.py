# Solução do exercício 8 da lista de exercícios da Aula 6
N = int(input('Digite um inteiro: '))
while N <= 1:
    print(f'{N} é inválido. Digite outro')
    N = int(input('Digite um inteiro: '))
    
if N == 2:
    print(f'{N} é primo')
elif N % 2 == 0:
    print(f'{N} não é primo')
else:
    cont = 0
    i = 3
    while i < N:
        if N % i == 0:
            print(i)
            cont += 1
        i += 2
    if cont == 0:
        print(f'{N} é primo')        
    else:
        print(f'{N} não é primo')        
        


print('\n\nFim do Programa')
