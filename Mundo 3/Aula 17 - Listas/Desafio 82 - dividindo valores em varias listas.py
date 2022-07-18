#Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares 
# e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas
lista = []
listaPar = []
listaImpar = []

while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)

    if valor % 2 == 0:
        listaPar.append(valor)
    elif valor % 2 == 1:
        listaImpar.append(valor)

    continuar = str(input("Quer continuar [S/N]? "))
    if continuar in 'Nn':
        break

print(f'Lista com todos os valores digitados {lista}')
print(f'Lista apenas com os valores pares digitados {listaPar}')
print(f'Lista apenas com os valores impares digitados {listaImpar}')