from venv import create


def arquivoExiste(nome):
    try: 
        a = open(nome, 'rt') # A abre o arquivo e tenta ler ele ('r = read t = text', por isso 'rt')
        a.close()# dps fecha o arquivo se tudo der certo
    except FileNotFoundError:
        return False # se o arquivo nao existir, ele retorna falso para a funcao arquivoExiste
    else: return True #se o arquivo existir, ele retorna verdadeiro para a funcao arquivoExiste

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')# ('w = write t = text', tenta escrever um texto. O mais(+) serve para caso o arquivo nao existe, ele crie um arquivo e abra-o)
        a.close()
    except:
        print('Ouve um erro na criacao do arquivo!')
    else:
        print('Arquivo criado com sucesso!')

def lerArquivo(nome):
    try:
        a =  open(nome,'rt')
    except:
        print('ERRO ao ler arquivo!')
    else:
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', ' ')
            print(f'{dado[0]:<20}{dado[1]:>3}anos')
    finally:
        a.close()

def cadastroPessoa(arq, nome = '<desconhecido>', idade = 0):
    try:
        a = open(arq, 'at') #'a' append 't' text
    except:
        print('ERRO ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO ao escrever os dados no arquivo!')
        else:
            print(f'Registro de {nome} adicionado!')
            a.close()
    
