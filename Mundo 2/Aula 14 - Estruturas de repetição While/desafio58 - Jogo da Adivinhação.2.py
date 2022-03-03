#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
from time import sleep

print('Vou pensar num número entre 0 e 10')
print('Hmmm... Pensando...')
print('Já sei!!! Tente adivinhar qual número estou pensando!\n')
escolha = random.randint(0, 10)
tentativas = 0

acertou = False
while not acertou:
    jogada = int(input('Qual o seu palpite? '))
    tentativas += 1
    if jogada == escolha:
        acertou = True
    else: 
        if jogada < escolha:
            print('Mais...')
        elif jogada > escolha:
            print('Menos...')
        
print(f'Acertou com {tentativas} tentativas!!!')
