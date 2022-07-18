#Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                                                                                                
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
continuar = 'S'

while continuar != 'N':
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    continuar = str(input("Quer continuar [S/N]? ")).strip().upper()
    lista.sort(reverse=True)
print(f'Um total de {len(lista)} numeros foram digitados')

print(f'\nLista de valores, ordenada de forma decrescente {lista}')

if 5 in lista:
    print(f'O valor 5 foi digitado na lista')
else:
    print("\nO valor 5 nao foi digitado na lista")