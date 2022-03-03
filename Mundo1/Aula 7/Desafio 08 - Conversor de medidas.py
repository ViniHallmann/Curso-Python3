#Escreva um programa que leia um valor em metro 
#e o exiba convertido em centímetros e milímetros

print('Conversor de metros para centímetro e milímetros')
a = float (input ('Digite o valor em metros: '))
b = (a)*100
c = (a)*1000
print(f'O valor de {a} metros para centímetros é de {b}cm')
print(f'O valor de {a} metros em milímetro é de {c}mm')