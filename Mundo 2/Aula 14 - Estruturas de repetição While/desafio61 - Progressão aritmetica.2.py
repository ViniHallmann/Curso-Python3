#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Gerador de PA')
p = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
termo = p
cont = 1
while cont <= 10:
    print(f'{termo} ⮞ ', end = '')
    termo = termo + r
    cont += 1
print (' FIM')