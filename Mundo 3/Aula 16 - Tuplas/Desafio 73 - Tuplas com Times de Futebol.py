#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
# Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do Internacional.
Tabela = ['Corinthians','Santos','América-MG','Bragantino','São Paulo',
'Atlético-MG','Botafogo','Internacional','Coritiba','Avaí','Cuiabá','Athletico-PR','Palmeiras',
'Flamengo','Fluminense','Goiás','Ceará','Juventude','Atlético Goianiense','Fortaleza']
print(f'Lista de Times do Brasileirao: {Tabela}')
print('--'*15)
print('Os 5 primeiros times da Tabela sao', Tabela[0:5],)  
print('--'*15) 
print('Os últimos 4 colocados sao', Tabela[16:],)
print('--'*15)
print('Times em ordem alfabética:', sorted(Tabela), )
print('--'*15)
print('O Internacional esta na posição',Tabela.index('Internacional'))
print(f'O Internacional esta na {Tabela.index("Internacional")} posicao')