#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o valor do seu sálario: '))
if salario <=1250.0:
    aumento = salario * 0.15
    valor_final = aumento + salario
if salario > 1250.0:
    aumento = salario * 0.10
    valor_final = aumento + salario

print(f'O seu sálario agora é de {valor_final} reais')
