#Faça um programa que tenha uma função chamada contador(), 
# que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:    
from time import sleep
def contador(a, b, c): 
    if c < 0:
        c*=-1
    if c == 0:
        c = 1
    print(f'Contagem de {a} ate {b} de {c} em {c}')
    
    if a < b:
        cont = a  
        while cont <= b:
            print(f'{cont}', end = ' ')
            cont += c 
        print("\nFIM!")
    else: 
        cont = a  
        while cont >= b:
            print(f'{cont}', end = ' ')
            cont -= c 
        print("\nFIM!")


#Programa principal
contador(1,10,1)
contador(10,1,1)
print("Agora e sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
print()
contador(inicio,fim,passo)

