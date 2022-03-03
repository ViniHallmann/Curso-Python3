#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
for par in range(2,52,2):
    print(par, end =' ')
print('')
for PAR in range(1,51):
    if PAR % 2 == 0:
        print(PAR, end = ' ')