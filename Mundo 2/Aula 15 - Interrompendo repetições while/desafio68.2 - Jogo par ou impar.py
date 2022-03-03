import random
contador = 0
while True :
    numero = int(input('Escolha um número de 0 a 10: '))
    escolha = str(input('PAR OU ÍMPAR?[P/I] ')).strip().upper()[0]
    Ncomputador = random.randint(0,10)
    total = numero + Ncomputador
    print(f'Você jogou {numero} e o computador jogou {Ncomputador}, total igual a {total}')
    if escolha == 'P' and total % 2 == 0 or escolha == 'I' and total % 2 == 1:
            print(f'Você ganhou!!!')
            contador += 1
    elif escolha == 'P' and total % 2 == 1 or escolha == 'I' and total %2 == 0:
            print(f'Você perdeu!!!')
            break
if contador == 1:
    print(f'Você teve apenas uma vitória...')
else:
    print(f'Você teve {contador} vitórias consecutivas')