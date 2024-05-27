A = int(input('Digite A: '))
B = int(input('Digite B: '))

print('Cálculos simples')
R = A + B
print(f'{A} + {B} = {R}')
R = A - B
print(f'{A} - {B} = {R}')
R = A * B
print(f'{A} * {B} = {R}')
R = A / B
print(f'{A} / {B} = {R}')
R = A // B
print(f'{A} // {B} = {R}')
R = A % B
print(f'{A} % {B} = {R}')
R = A ** B
print(f'{A} ** {B} = {R}')

print('\nCálculos mais complexos')
R = 2 * A - 3 * B
print(f'2 * {A} - 3 * {B} = {R}')
R = 2 * A + B
print(f'2 * {A} + {B} = {R}')
R = 2 * (A + B)
print(f'2 * ({A} + {B}) = {R}')

print('\n\nFim do Programa')
