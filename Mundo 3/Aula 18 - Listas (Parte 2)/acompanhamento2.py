#teste = list()
#teste.append('Vini')
#teste.append(19)

#galera = list()
#galera.append(teste[:])
#teste[0] = 'Maria'
#teste[1] = 22
#galera.append(teste[:])
#print(galera)

#Outro jeito de fazer lista dentro de lista
#galera = [['Joao',19],['Maria',19],['Pedro',19],['Lucas',19]]

#print(galera)

#for p in galera:
    #print(f'{p[0]} tem {p[1]} anos de idades')

galera = list()
dados = list()
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
galera.append(dados[:])
dados.clear()
print(galera)
for p in galera:
    if p[1] >=21:
        print(f'{p[0]} e maior de idade')
    else:
        print(f'{p[1]} e maior de idade')