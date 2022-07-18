#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
# ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)
import string


def leiaInt(msg):
    numero = 0
    ok = False
    while True:
        num = str(input(msg))
        if num.isnumeric():
            numero = int(num)
            ok = True
        else:
            print('ERRO! Digite um numero inteiro valido.')
        if ok == True:
            break
    return numero

num = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {num}')