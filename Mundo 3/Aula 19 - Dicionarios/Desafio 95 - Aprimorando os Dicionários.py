#Aprimore o desafio 93 para que ele funcione com vários jogadores, 
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
time = list()
golsList = list()
contador = 0

while True:
    golsList.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    while True:
        golsList.append(int(input(f'    Gols na partida {contador+1}: ')))
        jogador['gols'] = golsList[:]
        jogador['total'] = sum(jogador['gols'])
        contador += 1
        if (contador >= partidas):
            break
    time.append(jogador.copy())
    contador = 0
    print(f'Cadastro: {jogador}')
    
    continuar = str(input("Quer continuar [S/N]?")).strip().upper()
    if continuar == 'N':
        break

print("COD. NOME       GOLS    TOTAL")
print("-"*30)
for k,v in enumerate(time):
    print(f'{k:<5}', end =' ')
    for d in v.values():
        print(f'{str(d):<10}', end='')
    print()
while True:
    busca = int(input(("Mostrar dados de qual jogador (999 para parar)? ")))

    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Nao existe jogador com codigo {busca}')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"].capitalize()}')
        print("-"*30)
        for d,g in enumerate(time[busca]['gols']):
            print(f'No jogo {d+1}: Fez {g} gols')
            





#for k,v in jogador.items():
    #print(f'    O campo {k} tem o valor {v}')
#print(f'O jogador {"nome"} jogou {partidas}.')
#for p,g in enumerate(jogador['gols']):
    #print(f'=> Na partida {p+1}, fez {g} ')