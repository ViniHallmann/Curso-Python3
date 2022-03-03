#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, 
# pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
# programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('-'*14)
print('BANCO HALLMANN')
print('-'*14)

valor = int(input('Qual o valor que deseja sacar: R$'))
total = valor
nota = 50
cont = 0

while True:
    if total >= nota:
        total -= nota
        cont += 1
    else:  
        if cont > 0:
            print(f'Total de {cont} cédulas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        cont = 0
        if total == 0:
            break
    