#EX03

mes = input('Digite o Mês: ')

if (mes == '2' ):
    print('28')
elif (mes == '11' or mes == '4' or mes == '6' or mes == '9'):
    print('30')
elif (mes == '1' or mes == '3' or mes == '5' or mes == '7' or mes == '8' or mes == '10' or mes == '12'):
    print('31')
else:
    print('Digite um mês')
