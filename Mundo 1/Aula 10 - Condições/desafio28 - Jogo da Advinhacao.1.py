#programa que "pense" em um número inteiro de 0 a 5 e faça o usuario tentar descobrir qual foi o número que o computador escolheu
import random
from time import sleep
print('-=-'*10)
print('VOU PENSAR EM UM NÚMERO DE 0 A 5')
print('-=-'*10)
computador = random.randint(0, 5)
print('Tente descobrir qual número eu pensei!')
print('-=-'*10)
num = int(input('Que número que estou pensando? '))
print('PROCESSANDO...')
sleep(2)#faz o computador "durmir"
if num == computador:
    print('Você acertou, PARABÉNS!')
else:
    print(f'GANHEI, eu pensei no número {computador} e não no número {num}')
