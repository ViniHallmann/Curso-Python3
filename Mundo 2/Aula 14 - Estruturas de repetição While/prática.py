n = 1
PAR = 0
ÍMPAR = 0
while n !=0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            PAR += 1
        else:
            ÍMPAR += 1
print(f'Você digitou {PAR} números pares e {ÍMPAR} números ímpares.')