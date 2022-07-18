#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
contagem = ['Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis','Sete','Oito','Nove', 'Dez', 'Onze', 'Doze', ' Treze', 'Quatorze', 'Quinze',' Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte']
print(contagem[:])

while True:
    a = int(input("Digite um numero de Zero a Vinte: "))
    if 0 <= a <= 20:
        break
    print('Tente Novamente.', end =' ')
print(contagem[a])