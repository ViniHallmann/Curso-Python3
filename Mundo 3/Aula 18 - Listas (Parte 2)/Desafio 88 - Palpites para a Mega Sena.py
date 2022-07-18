#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
contadorJogos = 0
contadorNum = 0
lista = list()
jogos = list()
print('-'*20)
print('  JOGO DA MEGASENA')
print('-'*20)
numJogos = int(input("Quantos jogos voce que que eu sorteie? "))

while True:
    contadorNum = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            contadorNum+=1
        if contadorNum >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

    contadorJogos+=1
    if contadorJogos >= numJogos:
            break
print("\nOs jogos sorteados foram... \n")
sleep(1)
print(jogos)
for i, j in enumerate(jogos):
    print(f'{j}')
    sleep(1)
print()

