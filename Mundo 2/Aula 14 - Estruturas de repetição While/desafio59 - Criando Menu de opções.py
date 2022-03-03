n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opção = 0
from time import sleep
while opção != 5:
    print('''[1] Somar       (+)
[2] Subtrair    (-)
[3] Maior número
[4] Novos valores   
[5] Sair do Programa''')
    opção = int(input('Qual a sua opção? '))
    if opção == 1:
        print(f'A soma de {n1:.1f} + {n2:.1f} é igual a {n1+n2:.2f} ')
        sleep(1)
    if opção == 2:
        print(f'A subtração de {n1:.1f} - {n2:.1f} é igual a {n1-n2:.1f} ')
        sleep(1)
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print(f'O maior número dos dois valores é {maior}')
            sleep(1)
    if opção == 4:
        print('Digite novos valores: ')
        n1 = int(input('Primeiro valor: '))
        n1 = int(input('Segundo valor: '))
        sleep(1)
print('Saindo do programa!')