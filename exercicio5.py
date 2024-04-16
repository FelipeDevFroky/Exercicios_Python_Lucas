#Exercício 3

import math

num = int(input('Digite um número: '))

if(num > 0):
    num = math.sqrt(num)
    num_limitado = round(num, 2)
    print(num_limitado)
else:
    print('Número inválido')
