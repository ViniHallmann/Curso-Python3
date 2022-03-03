#criar o jogo do pedra papel e tesoura
from random import choice

print('''Suas opções são:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
jogada = int(input('Qual a sua jogada? '))

lista = [1,2,3]
computador = choice(lista) #escolha aleatória do computador

#Opção Inválida
if jogada != 1 and jogada != 2 and jogada != 3:
    print('Opção de jogada inválida. Tente novamente!')

#Temporizador
from time import sleep
if jogada == 1 or jogada == 2 or jogada ==3:
        print('JO')
        sleep(0.6)
        print('KEN')
        sleep(0.6)
        print('PO!')
        sleep(0.4)

#Primeira parte do jogo (EMPATE)
if jogada == 1 and computador == 1:
    print('='*22)
    print(f'Computador jogou Pedra')
    print(f'Jogador    jogou Pedra')
    print('='*22)
    print('       !EMPATE!')
elif jogada == 2 and computador == 2:
    print('='*22)
    print(f'Computador jogou Papel')
    print(f'Jogador    jogou Papel')
    print('='*22)
    print('       !EMPATE!')
elif jogada == 3 and computador == 3:
    print('='*24)
    print(f'Computador jogou Tesoura')
    print(f'Jogador    jogou Tesoura')
    print('='*24)
    print('        !EMPATE!')

#Segunda parte do jogo (Vitória JOGADOR)
if jogada == 1 and computador == 3:
    print('='*24)
    print(f'Computador jogou Tesoura')
    print(f'Jogador    jogou Pedra')
    print('='*24)
    print('    !JOGADOR VENCEU!')
if jogada == 2 and computador == 1:
    print('='*22)
    print(f'Computador jogou Pedra')
    print(f'Jogador    jogou Papel')
    print('='*22)
    print('   !JOGADOR VENCEU!')
if jogada == 3 and computador == 2:
    print('='*24)
    print(f'Computador jogou Pedra')
    print(f'Jogador    jogou Tesoura')
    print('='*24)
    print('   !JOGADOR VENCEU!')

#Terceira parte do jogo (Vitória COMPUTADOR)
if jogada == 3 and computador == 1:
    print('='*24)
    print(f'Computador jogou Pedra')
    print(f'Jogador    jogou Tesoura')
    print('='*24)
    print('  !COMPUTADOR VENCEU!')
if jogada == 1 and computador == 2:
    print('='*22)
    print(f'Computador jogou Papel')
    print(f'Jogador    jogou Pedra')
    print('='*22)
    print('  !COMPUTADOR VENCEU!')
if jogada == 2 and computador == 3:
    print('='*24)
    print(f'Computador jogou Tesoura')
    print(f'Jogador    jogou Papel')
    print('='*24)
    print('   !COMPUTADOR VENCEU!')

