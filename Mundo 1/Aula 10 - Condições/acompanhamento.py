#condições simples e compostas 
#if carro.esquerda():
   # bloco true
#else:
   # bloco false

#Maneiras diferentes de escrever
tempo = int(input('Quanto anos tem seu carro:'))
if tempo <=3:
    print("Carro novo")
else:
   print('Carro velho')
print('--FIM--')

tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')