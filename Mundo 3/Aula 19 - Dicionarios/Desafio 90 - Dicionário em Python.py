#Faça um programa que leia nome e média de um aluno, 
#guardando também a situação em um dicionário. 
#No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input("Media: "))

#print(f'Nome do aluno: {aluno["nota"]}')
#print(f'Media do aluno: {aluno["media"]}')
if aluno['media'] >= 6:
    aluno['situacao'] = str('aprovado')
else:
    aluno['situacao'] = str('reprovado')
for k, v in aluno.items():
    print(f'- {k} igual a {v}')