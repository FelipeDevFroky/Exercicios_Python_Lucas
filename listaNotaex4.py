a = float(input('Digite o valor de A: '))

if (a == 0):
    print('A equação não é de segundo grau')
    exit()
    
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
delta = (b ** 2) - 4 * (a * c)
print(delta)
if delta < 0:
    print('A equação não possui raizes reais')
    exit()
if delta == 0:
    print('possui apenas 1 raiz')
if delta > 0:
    print('possui 2 raizes reais ')
    raizdelta = delta ** 0.5
    print('Raiz de delta',raizdelta)
    x1 = (-b + raizdelta) / (2 * a)
    x2 = (-b - raizdelta) / (2 * a)
    print('x1',x1)
    print('x2',x2)

