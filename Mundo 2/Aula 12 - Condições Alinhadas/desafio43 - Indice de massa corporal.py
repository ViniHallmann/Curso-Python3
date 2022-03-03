#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
# e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
##– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
print('CALCULADORA DE IMC')
altura = float(input('Digite sua altura atual(Metros): '))
peso = float(input('Digite o seu peso atual(KG): '))
imc = peso / (altura ** 2)
print(f'O seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif imc >= 18.5 and imc < 25:
    print('Você está em um peso ideal')
elif imc > 25 and imc < 30:
    print('Você está com sobrepeso')
elif imc > 30 and imc < 40:
    print('Você está com obesidade')
else: 
    print('Você está com obesidade morbida')