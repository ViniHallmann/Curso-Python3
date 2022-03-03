#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
print('='*30)
print('        LOJA DO VINÃO')
print('='*30)
somaT = maior = menor = contador = 0
soma1000 = 0
barato = ''
while True:
    nomeP = str(input('Nome do produto: '))
    preçoP = float(input('Preço do produto: R$ '))
    contador += 1
    somaT += preçoP
    if preçoP > 1000:
        soma1000 += 1
    if contador == 1:
        menor = preçoP
        barato = nomeP
    else: 
        if preçoP < menor:
            menor = preçoP
            barato = nomeP
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar not in 'SN':
            print('Opção inválida. Tente Novamente!')
    if continuar == 'N':
        break
print(f'O total da compra é de R$ {somaT}')
if preçoP > 1000:
    print(f'Temos {soma1000} produto custando mais de R$ 1000')
print(f'O nome do produto mais barato é {barato.capitalize()}')
    
        
