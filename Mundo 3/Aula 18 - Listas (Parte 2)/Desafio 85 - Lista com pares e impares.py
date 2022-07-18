#Crie um programa onde o usuário possa digitar sete valores numéricos 
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[],[]]

for a in range(1,8):
    valor = int(input(f'Digite o {a}o. valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
        lista[0].sort()
    if valor % 2 == 1:
        lista[1].append(valor)
        lista[1].sort()

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores pares digitados foram: {lista[1]}')