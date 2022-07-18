from random import randint
from time import sleep
from operator import itemgetter

jogador = dict()
ranking = list()
print("Quem comeca jogando primeiro? Jogando os dados... ")
sleep(1)
jogador['1'] = randint(1,6)
jogador['2'] = randint(1,6)
jogador['3'] = randint(1,6)
jogador['4'] = randint(1,6)

for k,v in jogador.items():
    print(f'Jogador {k} tirou {v}')
    sleep(0.8)

ranking = sorted(jogador.items(), key = itemgetter(1), reverse = True)
print("Quem joga primeiro? ")
for i,v in enumerate(ranking):
    print(f'{i+1} Lugar:  Jogador {v[0]}')
    sleep(0.8)


