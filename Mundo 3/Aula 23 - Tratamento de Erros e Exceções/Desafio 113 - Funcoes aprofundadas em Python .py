#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da 
# digitação de um número de tipo inválido. Aproveite e 
# crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um numero inteiro valido.')
            continue
        else:
            return num


def leiaReal(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um numero real valido.')
            continue
        else:
            return num

inteiro = leiaInt('Digite um numero inteiro: ')
real = leiaReal('Digite um numero real: ')
print(f'Voce acabou de digitar o numero {inteiro} e o valor real foi {real}')
