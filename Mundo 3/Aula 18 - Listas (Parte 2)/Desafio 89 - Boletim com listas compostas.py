#Crie um programa que leia nome e duas notas de vários alunos 
# e guarde tudo em uma lista composta. No final, mostre um boletim 
# contendo a média de cada um 
#  permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = []
continuar = 'S'
while True: 
    aluno = str(input("Nome: "))
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 1: "))
    media = (nota1 + nota2)/2
    lista.append([aluno,nota1,nota2,media])
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()
    if continuar in 'N':
        break
    
print('No.      NOME        MEDIA')
print('-'*26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0].capitalize():>9}{a[3]:>13}')
while True:
    verNota = int(input("Mostrar nota de algum aluno? [999 interrompe] "))
    if verNota == 999:
        print("TERMINO DO PROGRAMA...")
        break
    print(f'Notas de {lista[verNota][0]} sao [{lista[verNota][1]}, {lista[verNota][2]}]')
    

