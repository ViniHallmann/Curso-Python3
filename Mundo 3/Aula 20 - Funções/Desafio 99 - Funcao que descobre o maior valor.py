#Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros.
#  Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(*valores):
    contador = maior = 0
    print("Analisando os valores passados...")
    for numero  in valores:
        print(f'{numero}', end = ' ', flush = True)
        sleep(0.3)
        if contador == 0:
            maior = numero
        else:
            if numero > maior:
                maior = numero
        contador +=1
    print(f'\nForam informados {contador} numeros ao todo')
    print(f'O maior numero informado foi {maior}')


maior(0,9,4,3)
