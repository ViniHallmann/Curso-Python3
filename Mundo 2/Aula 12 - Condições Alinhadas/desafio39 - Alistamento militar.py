#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#  se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
ano = int(input('Digite o ano em que você nasceu: '))
ano_atual = datetime.date.today().year #diz em que anos estamos
idade = ano_atual - ano #calcula idade
data = ano + 18
menor = data - ano_atual #calcula quanto tempo falta para o alistamento
maior = (data + idade) - idade
print(f'Pessoas nascidas {ano} já possuem, ou iram fazer, {idade} anos de idade em {ano_atual}')
if idade == 18:
    print(f'Você deve se alistar o quanto antes!!')

if idade == 17:
    print(f'Ainda falta 1 ano para o seu alistamento')
    print(f'Seu alistamento será ano que vem, em {ano_atual +1}')

elif idade < 18:
    print(f'Ainda faltam {menor} anos para o seu alistamento')
    print(f'Seu alistamento será em {data}')

else:
    print(f'Você já deveria ter se alistado há {ano_atual - maior} anos')
    print(f'Seu alistamento ocorreu no ano de {maior}')