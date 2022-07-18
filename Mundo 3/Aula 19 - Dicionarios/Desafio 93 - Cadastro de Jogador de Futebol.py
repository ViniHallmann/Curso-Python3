#Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
#O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. 
#No final, tudo isso será guardado em um dicionário, 
#incluindo o total de gols feitos durante o campeonato.

jogador = dict()
golsList = list()
contador = 0


jogador['nome'] = str(input("Nome do jogador: "))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

while True:
    golsList.append(int(input(f'Gols na partida {contador+1}: ')))
    jogador['gols'] = golsList[:]

    contador += 1
    if (contador >= partidas):
        break
contador = 0
print(f'Dicionario: {jogador}')
jogador['total'] = sum(jogador['gols'])
for k,v in jogador.items():
    print(f'    O campo {k} tem o valor {v}')
print(f'O jogador {"nome"} jogou {partidas}.')
for p,g in enumerate(jogador['gols']):
    print(f'=> Na partida {p+1}, fez {g} ')