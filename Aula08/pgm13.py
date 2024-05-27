# Solução do exercício 13 da lista de exercícios da Aula 9

def EPrimo(valor):
    if valor == 2:
        return True
    elif valor % 2 == 0:
        return False
    else:
        i = 3
        while i < valor:
            if valor % i == 0:
                return False
            i += 2
        return True
    

N = int(input('Digite N: '))
Primos = []
Candidato = 2

# Solução usando uma função capaz de verificar se Candidato é primo
a = 0
while a < N:
    if EPrimo(Candidato):
        Primos.append(Candidato)
        a += 1
    Candidato += 1

# Solução sem uso de função, com a verificação dos primos no próprio corpo do código de controle
"""
a = 0
while a < N:
    if Candidato == 2:
        Primos.append(Candidato)
        a += 1
    elif Candidato % 2 == 1:
        cont = 0
        i = 3
        while i < Candidato:
            if Candidato % i == 0:
                cont += 1
            i += 2
        if cont == 0:
            Primos.append(Candidato)
            a += 1
    Candidato += 1
"""        
      

print(f'\nLista dos {N} primeiros primos')
print(Primos)

print('\n\nFim do Programa')
