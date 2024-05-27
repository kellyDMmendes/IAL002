# Solução do exercício 4 da lista de exercícios da Aula 6

N = int(input('Digite N: '))
valsValidos = False
i = 0
while i < N:
    X = float(input(f'Digite o elemento {i}: '))
    if X > 0:
        if not valsValidos:  # na primeira vez esse objeto é falso
            guardaMenor = guardaMaior = X
        valsValidos = True
        if X < guardaMenor:
            guardaMenor = X
        if X > guardaMaior:
            guardaMaior = X
    else:
        print(f'  valor {X} é inválido')

    i += 1

if valsValidos:   #  é o mesmo que valsValidos == True <-- mas essa forma não se usa
    print(f'Menor valor = {guardaMenor}')
    print(f'Maior valor = {guardaMaior}')
else:
    print('Não foram fornecidos valores válidos')

print('\n\nFim do Programa')
