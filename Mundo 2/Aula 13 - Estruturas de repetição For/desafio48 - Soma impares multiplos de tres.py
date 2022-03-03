#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
for contagem in range(1,501,2):
    if contagem % 3 == 0:
        soma += contagem 
        print(contagem, end = ' ')

print(f'\nA soma dos valores é {soma}')
