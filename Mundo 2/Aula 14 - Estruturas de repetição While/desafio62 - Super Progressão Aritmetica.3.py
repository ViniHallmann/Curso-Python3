#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
#O programa encerrará quando ele disser que quer mostrar 0 termos.
print('Gerador de PA')
p = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ⮞ ', end = '')
        termo = termo + razão
        cont += 1
    print(' PAUSA')
    mais = int(input('Deseja ver mais algum termo da PA? Se sim digite o valor desejado, se não, digite 0 para encerrar o gerador de PA: '))
print(f'{total} Termos da PA foram mostrados')
print('GERADOR ENCERRADO')