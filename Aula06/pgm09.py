# Solução do exercício 9 da lista de exercícios da Aula 6

arq = open('Aula06/saida_pgm09.txt', 'w')
N = int(input('Digite a quantidade de termos: '))
A = 0
B = 1
i = 0
while i < N:
    print(A)
    arq.write(f'{A}\n')
    C = A + B
    A = B
    B = C
    i += 1
arq.close()

print('\n\nFim do Programa')
