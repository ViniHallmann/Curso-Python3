#Modifique as funções que foram criadas no desafio 107 para que 
# elas aceitem um parâmetro a mais, informando se o valor 
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda
valor = float(input("Digite o preco: R$"))
print(f'A metade de R${moeda.moeda(valor)} é R${(moeda.metade(valor, True))}')
print(f'O dobro de R${moeda.moeda(valor)} é R${(moeda.dobro(valor, True))}')
print(f'Aumentando 10%, temos R${(moeda.aumentar(valor, True))}')