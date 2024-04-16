#EX04

mais = '+'
menos = '-'
vezes = '*'
divisao = '/'

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

operacao = str(input('Digite a operação desejada: '))

if (operacao == mais):
    print(num1 + num2)
elif (operacao == menos):
    print(num1 - num2)
elif (operacao == vezes):
    print(num1 * num2)
elif (operacao == divisao):
    print(num1 / num2)
else:
    print('Operação não válida, tente novamente')
    
