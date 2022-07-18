import funcoes
from time import sleep
import arquivo

arq = 'cursoemvideo.txt'
if arquivo.arquivoExiste(arq):
    print('-'*30)
    titulo = 'Arquivo encontrado'
    x = titulo.center(30)
    print(x)
    print('-'*30)
else:
    print('-'*30)
    titulo = 'Arquivo nao encontrado.'
    x = titulo.center(30)
    print(x)
    print('-'*30)
    print('-'*30)
    sleep(1)
    titulo = 'Criando arquivo...'
    x = titulo.center(30)
    print(x)
    print('-'*30)
    arquivo.criarArquivo(arq)

sleep(1)
#Programa Principal
while True:
    print(funcoes.menu('MENU PRINCIPAL'))
    opcao = funcoes.leiaInt('Opção: ')
    funcoes.opcao123(opcao)
    if opcao == 1:
        arquivo.lerArquivo(arq)
    if opcao == 2:
        nome = str(input('Nome: '))
        idade = funcoes.leiaInt('Idade: ')
        arquivo.cadastroPessoa(arq,nome,idade)
    if opcao == 3:
        break
    sleep(1.5)
    