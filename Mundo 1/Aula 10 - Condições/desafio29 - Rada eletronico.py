 #Escreva um programa que leia a velocidade de um carro. 
# #Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
 
velocidade = float(input('Qual a atual velocidade do carro? '))
multa = (velocidade - 80)*7
if velocidade <= 80:
    print('O carro está dentro da velocidade permitida, não há necessidade de multa.')
    print('Tenha um bom dia e dirija com segurança!')
else:
    print('O carro ultrapassou o limite de velocidade permitido, MULTADO!!')
    print(f'Você deve pagar uma multa de {multa:.2f} reais')
    print("Tenha um bom dia e dirija com segurança!")
