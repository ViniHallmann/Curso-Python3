from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input("Nome: "))
nascimento =int(input("Ano de nascimento: "))
trabalhador['idade'] = datetime.now().year - nascimento
trabalhador['ctps'] = int(input("Cod. Carteira de trabalho [0 nao tem]: "))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input("Ano de contratacao: "))
    trabalhador['salario'] = float(input("Salario: "))
    trabalhador['aposentadoria'] = trabalhador['idade']+ ((trabalhador['contratacao'] + 35) - datetime.now().year)

for k, v in trabalhador.items():
    print(f'- {k} tem o valor {v}')