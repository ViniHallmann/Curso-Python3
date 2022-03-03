#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print('='*22)
print('LEITOR DE NÚMERO PRIMO')
print('='*22)
n = int(input('Digite um número: '))
print('='*22)
divisores = 0
for a in range(1, n + 1):
    if n % a == 0:
        print('\033[31m', end = ' ')
        divisores += 1
    else:
        print('\033[m', end = ' ')
    print(f'{a}''\033[m', end = '')
print(end = '\n')
print('='*22)
print(f'O número {n} foi dívisivel {divisores} vezes.', end = ' ')

if divisores == 2:
    print('Esse número é \033[31mPRIMO!\033[m')
else:
    print('Esse número \033[31mNÃO\033[m é \033[31mPRIMO!\033[m')



    
