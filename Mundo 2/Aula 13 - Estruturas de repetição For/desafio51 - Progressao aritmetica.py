print('='*23)
print('  10 TERMOS DE UMA PA')
print('='*23)

n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = n1 +(10 -1)*r
for a in range(n1,decimo + r, r):
    print(f'{a} ⮞ ', end = ' ')
print('ACABOU!')