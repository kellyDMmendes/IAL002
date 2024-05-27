# Este programa gera 4 valores aleatórios sendo doi inteiros e dois reais.
# Esses 4 valores são gravados em uma linha do arquivo de saída, separados
#   pelo caractere ';'

from random import randint

Dados = []
Qtde = int(input('Digite a quantidade de linhas desejadas >> '))
print('Gerando dados')
for _ in range(Qtde):
    a = randint(1000, 9999)
    b = randint(1, 250)
    c = randint(5, 120) + randint(0, 99) / 100
    d = randint(0, 50) + randint(0, 999) / 1000
    Dados.append( [a, b, c, d] )

print('Gravando arquivo de saída')
arqSai = open('saida.txt', 'w')
for d in Dados:
    arqSai.write(f'{d[0]};{d[1]};{d[2]:.2f};{d[3]:.3f}\n')
arqSai.close()
print('Arquivo gravado')
print('\n\nFim do Programa')


