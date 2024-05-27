# Solução do exercício 10 da lista de exercícios da Aula 6

arq = open('Aula06/saida_pgm10.txt', 'w')
N = int(input('Digite a quantidade de termos: '))
Prim = int(input('Digite Prim: '))
arq.write(f'Sequência de Fibonacci\n')
arq.write(f'A seguir temos o {N} elementos maiores que {Prim}\n\n')
A = 0
B = 1
i = 0
while i < N:
    if A > Prim:
        print(A)
        arq.write(f'{A}\n')
        i += 1
    C = A + B
    A = B
    B = C
arq.close()

print('\n\nFim do Programa')
