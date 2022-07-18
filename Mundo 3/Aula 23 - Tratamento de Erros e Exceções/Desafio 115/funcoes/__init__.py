def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um numero inteiro valido.')
            continue
        else: 
            return numero

def menu(titulo):
    print('-'*30)
    tituloMenu = titulo
    x = tituloMenu.center(30)
    print(x)
    print('-'*30)
    print('1 - Ver pessoas cadastradas \n2 - Cadastras nova Pessoa \n3 - Sair do Sistema')
    print('-'*30)

def opcao123(num):
    if num == 1:
        print('-'*30)
        titulo = 'PESSOAS CADASTRADAS'
        x = titulo.center(30)
        print(x)
        print('-'*30)
        
    if num == 2:
        print('-'*30)
        titulo = 'NOVO CADASTRO'
        x = titulo.center(30)
        print(x)
        print('-'*30)
        
    if num == 3: 
        print('-'*30)
        titulo = 'SAINDO DO SISTEMA... ATE LOGO!'
        x = titulo.center(30)
        print(x)
        print('-'*30)