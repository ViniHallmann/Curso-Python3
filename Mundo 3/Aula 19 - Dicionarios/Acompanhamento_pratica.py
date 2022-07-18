pessoas = {'nome': 'Vinicius', 'idade': 19, 'sexo': 'M'}
print(pessoas['nome'])
#print formatado
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # tem que usar aspas dupla

#apagar elementos = del
del pessoas.items()
#inserir elemento 
pessoas['nome'] = 'Pedro' # mudou de vinicius para pedro 

for i in pessoas.keys():
    print(i)
print()
for i in pessoas.values():
    print(i)
print()
for i in pessoas.items():
    print(i)
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

#print(brasil)
print(brasil[0])
print(brasil[0]['uf'])