#Crie um programa que vai gerar cinco números aleatórios e 
# colocar em uma tupla. Depois disso, mostre a listagem de números gerados e 
# também indique o menor e o maior valor que estão na tupla.

from random import randint
n = (randint(0,10), randint(0,10), randint(0,10), randint(0,10),randint(0,10))
#for a in range(0,5):
    #n = (randint(0,10))
    #print(n, end =' ')
for a in n:
    print(f'{a} ', end ='')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
