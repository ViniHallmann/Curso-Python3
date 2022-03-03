#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
num = int(input('Digite um número para calcular o seu valor fatorial: '))
cont = num
print(f'Calculando {num}! = ', end = '')
while cont > 0: 
    print(f'{cont}', end = '')
    print( ' x ' if cont > 1 else ' = ', end = '' )
    cont -= 1
print(f'{factorial(num)}')