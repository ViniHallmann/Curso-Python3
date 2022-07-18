#Faça um programa que leia nome e peso de várias pessoas,         
#guardando tudo em uma lista. No final, mostre:                                                                                                    
#A) Quantas pessoas foram cadastradas.                               
#B) Uma listagem com as pessoas mais pesadas.                                                                                                    
#C) Uma listagem com as pessoas mais leves.
pessoas = []
dados = []
listaMaiorPeso = []
listaMenorPeso = []
maior = menor = 0
while True:
    nome = str(input("Nome: "))
    dados.append(nome)
    peso = float(input("Peso: "))
    dados.append(peso)
    
    
    if len(pessoas) == 0:
        maior = menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    pessoas.append(dados[:])
    dados.clear()
    
    continuar = str(input("Quer continuar [S/N]? "))
    if continuar in 'Nn':
        break

print(f'Voce cadastrou {len(pessoas)} pessoas')

for a in pessoas:
    if peso == maior:
        listaMaiorPeso.append(a[0])
    if peso == menor:
        listaMenorPeso.append(a[0])

print(f'O maior peso foi de {maior}Kg. Peso de {listaMaiorPeso}')
print(f'O menor peso foi de {menor}Kg. Peso de {listaMenorPeso}')

