estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    #brasil.append(estado[:]) # jeito certo usando lista
    brasil.append(estado.copy())
for estado in brasil:
    for k, v in estado.items():
        print(f'{k} = {v}')