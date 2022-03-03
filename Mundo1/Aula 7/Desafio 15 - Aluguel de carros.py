dias = int (input('Quantos dias alugados?'))
km = float (input('Quantos KM rodados?'))
total = (60*dias) + (km*0.15)
print(f'O total a se pagar pelo aluguel é de R$ {total}.')