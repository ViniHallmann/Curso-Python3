from optparse import Values


filme = {'titulo': 'Star Wars',
'ano': 1977,
'diretor': 'George Lucas'
}
#print(filme.values()) # values = star wars, 1997, george lucas
#print(filme.keys()) # keys = titulo, ano, diretor
#print(filme.items()) # items = tudo
for keys, values in filme.items():
    print(f'o {keys} e {values}')
