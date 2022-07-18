#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.
while True:
    print('-'*33)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*33)
    if n < 0:
        print("Programa Fechado")
        break
    for a in range(1,11):
        print(f'{n} X {a} = {n*a}')
    