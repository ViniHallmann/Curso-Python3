#Faça um algoriritmo que leia o salário de um funcionário 
#e mostre o seu novo salário com 15% de aumento.

print('Cálculo Salário')
a = float (input ('Insira seu salário bruto aqui: '))
b = float (a)*0.15
salario_final = int(a) + int(b)
print('Seu salário bruto com um aumento de 15% será de',salario_final,'reais')