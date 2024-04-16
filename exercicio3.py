#exercício 1

num = (int(input('Digite um número: ')))

if (num < 0 or num > 100):
    print('Só pode de 0 A 100')
elif (num>=86 and num<=100):
    print('A')
elif (num>=61 and num<=85):
    print('B')
elif (num>=36 and num<=60):
    print('C')
elif (num>=1 and num<=35):
    print('D')
elif (num==0):
    print('E')

