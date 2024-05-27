# Este programa lê um arquivo texto de entrada, no qual cada linha
#   contém dois inteiros e um real separador por ';'

Dados = []
arq = open('dados.txt', 'r', encoding='utf-8') # se o arquivo for ANSI, troque o enconding
s = arq.readline().rstrip()
while s != '':
    s = s.split(';')
    l = [int(s[0]),     # código do produto
         int(s[1]),     # qtde estoque
         float(s[2])    # preço unitário
         ]
    Dados.append(l)
    s = arq.readline().rstrip()
arq.close()
for d in Dados:
    print(d)


print('\n\nFim do Programa')


