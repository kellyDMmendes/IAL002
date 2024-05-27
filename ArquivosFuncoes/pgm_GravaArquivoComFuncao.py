# Este programa gera 4 valores aleatórios sendo doi inteiros e dois reais.
# Esses 4 valores são gravados em uma linha do arquivo de saída, separados
#   pelo caractere ';'
# A gravação do arquivo é feita em uma função

from random import randint

def LeNomeArq():
    '''Lê o nome do arquivo, garantindo que contenha a extensão .txt'''
    lido = input('Digite o nome do arquivo: ')
    while len(lido) <= 5 and lido[-4:].lower() != '.txt':
        print(f'  Erro! Nome inválido {lido}. Deve ter 1 caractere mais a extensão .txt')
        lido = input('Digite o nome do arquivo: ')
    return lido
    

def GravaArq(nome_arq, lista):
    '''grava a lista em arquivo com o nome nome_arq. O formato de cada elemento da lista deve ser int;int;float;float'''
    arqSai = open(nome_arq, 'w')
    for d in lista:
        arqSai.write(f'{d[0]};{d[1]};{d[2]:.2f};{d[3]:.3f}\n')
    arqSai.close()    

def GeraDados():
    for _ in range(Qtde):
        a = randint(1000, 9999)
        b = randint(1, 250)
        c = randint(5, 120) + randint(0, 99) / 100
        d = randint(0, 50) + randint(0, 999) / 1000
        Dados.append( [a, b, c, d] )

# Parte principal
Dados = []
Qtde = int(input('Digite a quantidade de linhas desejadas >> '))
print('Gerando dados')
GeraDados()
print('Gravando arquivo de saída')
nome = LeNomeArq()
GravaArq(nome, Dados)
print('Arquivo gravado')
print('\n\nFim do Programa')


