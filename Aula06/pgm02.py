# Solução do exercício 2 da lista de exercícios da Aula 6

minimo = int(input('Digite o mínimo: '))
maximo = int(input('Digite o máximo: '))

if minimo > maximo:
    print('Erro!!! O mínimo deve ser menor ou igual ao máximo')
else:
    print(f'\nDivisíveis por 5 na faixa [{minimo}, {maximo}]')
    valor = minimo
    while valor <= maximo:
        if valor % 5 == 0:
            print(valor)
        valor += 1


print('\n\nFim do Programa')
