#Faça um programa que leia a a altura e largura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2m²

print ('Calculadora de tinta ')
a = float (input('Quanto de altura a parede que será pintada têm (em metros)?'))
b = float (input('Quanto de largura a parede que será pintada têm (em metros)?'))
c = a*b
d = float (c)/2
print(f'Área da parede = {c}m²')
print(f'Você precisa comprar um total de {d:.2f} litros de tinta')