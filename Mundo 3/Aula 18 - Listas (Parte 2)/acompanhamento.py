    #dados = []
    #dados.append('Pedro')
    #dados.append(25)
    #pessoas = []
    #pessoas.append(dados[:])

#outro jeito de fazer 
#              0               1            2
pessoas = [['pedro',25],['Maria', 19],['Joao',32]]
#             0      1      0      1      0   1

print(pessoas[0][0]) # pessoa 0 e imprime o Pedro
print(pessoas[1][0]) # imprime pessoa 1 e imprime 19
print(pessoas[2][0]) # imprime pessoa 2 e imprime Joao
print(pessoas[1]) # imprime pessoa 1 e tudo que tem nela
