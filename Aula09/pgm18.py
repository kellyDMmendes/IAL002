# Solução do exercício 18 da lista de exercícios da Aula 9

minimo = int(input('Digite o mínimo: '))
maximo = int(input('Digite o máximo: '))
while minimo >= maximo:
    print('  o máximo deve ser maior que mínimo')
    maximo = int(input('Digite o máximo: '))

i = minimo
while i <= maximo:
    if i % 7 == 0:
        print(i)
    i+=1

print('\n\nFim do Programa')
