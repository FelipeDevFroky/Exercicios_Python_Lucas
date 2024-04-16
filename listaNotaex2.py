num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))


if (num1 > num2 and num1 > num3):
    print('número maior: ' , num1)
elif (num2 > num1 and num2 > num3):
    print('número maior: ' , num2)
elif (num3 > num1 and num3 > num2):
   print('número maior: ' , num3)
   
   
if (num1 < num2 and num1 < num3):
    print('número menor: ' , num1)
elif (num2 < num1 and num2 < num3):
   print('número menor: ' , num2)
elif (num3 < num1 and num3 < num2):
   print('número menor: ' , num3)

