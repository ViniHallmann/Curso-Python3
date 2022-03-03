#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
contador = 0
while True :
    numero = int(input('Escolha um número de 0 a 10: '))
    Ncomputador = random.randint(0,10)
    total = numero + Ncomputador
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('PAR OU ÍMPAR?[P/I] ')).strip().upper()[0]
    print(f'Você jogou {numero} e o computador jogou {Ncomputador}, total igual a {total}')
    if escolha == 'P':
        if total % 2 == 0:
            print(f'Você jogar PAR e ganhou!!!')
            contador += 1
        else:
            print('Você jogou PAR e perdeu!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print(f'Você jogou ÍMPAR e ganhou!!!')
            contador += 1
        else:
            print('Você jogou ÍMPAR e perdeu!')
            break

print(f'Você teve {contador} vitórias consecutivas')