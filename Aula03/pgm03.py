A = 12
saida = 'O objeto A contém {} - feito com string formatado'.format(A)
print(saida)

B = 4
saida = f'O objeto B contém {B} - feito com f-string'
print(saida)

X = 187.37293824238
saida = f'O objeto X contém {X:.3f} - feito com f-string'
print(saida)

print('\nusando f-string direto dentro do print')
print(f'O objeto X contém {X:.3f} - feito com f-string')
