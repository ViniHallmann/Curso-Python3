#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

n1 = float(input('Digite sua nota de matemática: '))
n2 = float(input('Digite sua nota de português: '))

média = (n1 + n2 )/2
print(f'A sua média foi de {média:.2f} pontos')
if média < 5 :
    print('Você foi REPROVADO, estude mais!')
if média >= 7:
    print('Você foi APROVADO, parabéns!')
elif média >= 5 and média < 7:
    print('Você está de recuperação')
