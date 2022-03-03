from random import randint
rx = '\33[35m'
pt = '\33[0m'
az = '\33[47;34m'
az1 = '\33[47;34;7m'
az2 = '\33[34m'
vm = '\33[42;31m'
vm1 = '\33[41;32m'
vm2 = '\33[31m'
bc = '\33[41;37;7m'
bc1 = '\33[41;37m'
bc2 = '\33[41;37;3m'
vd = '\33[32m'
am = '\33[33m'
print('\n' + bc + '****' * 18 + pt)
print(vm1 + '  ' * 9 + '       JOGO COM BREAK - V 2.0              ' + ' ' * 11 + pt)
print(bc + '****' * 18 + pt + '\n')
print('{}/\/\{}'.format(vd, pt) * 14)   # Início
print('{}                VAMOS JOGAR PAR OU ÍMPAR{}'.format(rx, pt))
t = 0
while True:
    print('{}/\/\{}'.format(vd, pt) * 14 + '\n')
    c = randint(1, 10)
    while True:
        p = str(input('Diga um {0}valor{1}: '.format(vd, pt)))
        if p.isnumeric():
            break
    p = int(p)
    while True:
        n = str(input('{0}Par{1} ou {0}Ímpar{1} {2}[P/I]{1}: '.format(vd, pt, vm2))).lower().split()
        n = ''.join(n)
        n = n[0]
        if n == 'p' or n == 'i' or n == 's':
            break
    v = p + c
    if v % 2 == 0:
        k = 'p'
        m = 'PAR'
    else:
        k = 'i'
        m = 'ÍMPAR'
    print('\n' + '{}===={}'.format(vd, pt) * 14)
    print('Você jogou {0}{2}{1} e o computador {3}{4}{1}.'
          ' Total de {0}{5}{1} DEU {0}{6}{1}'.format(vd, pt, p, vm2, c, v, m))
    print('{}===={}'.format(vd, pt) * 14)
    if k != n:
        break
    else:
        print('Você {0}VENCEU{1}!'.format(vd, pt))
        print('{}Vamos jogar novamente...\n{}'.format(vd, pt))
    t += 1
if t == 1:
    o = ''
elif t == 0:
    o = ''
    t = 'NENHUMA'
else:
    o = 'es'
print('\nVocê {}PERDEU{}!'.format(vm2, pt))
print('{0}GAME OVER!{1} Você venceu {2}{3}{1} vez{4}.'.format(vm2, pt, vd, t, o))   # Fim
print('\n' + bc + '****' * 18 + pt)
print(vm1 + '  ' * 10 + '         FIM DO PROGRAMA                 ' + ' ' * 11 + pt)
print(bc + '****' * 18 + pt + '\n')