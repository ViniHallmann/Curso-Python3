lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
print(lanche[-1])

lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
print(lanche[0])
lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
print(lanche[1])

lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
print(lanche[1:])

lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
print(lanche[1:3])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
#print(len(lanche))
print(f'')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')