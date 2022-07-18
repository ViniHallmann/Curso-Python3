#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#  A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
def sorteio(lista):
    contador = 0
    print("Sorteando 5 valores da lista: ")
    while True:
        valores = randint(0,10)
        if valores not in lista:
            lista.append(valores)
            contador+=1
        if contador>= 5:
            break
    for valores in lista:
        print(f'{valores}', end = ' ', flush = True)
        sleep(0.4)
    print("Esses foram os valores sorteados!")    
def somaPar(lista):
    soma = 0
    print(f"Somando os valores pares de {lista}", end = '')
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f', temos {soma}')

lista = []
sorteio(lista)
somaPar(lista)

