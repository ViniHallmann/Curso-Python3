def fatorial(num):
    f = 1
    for c in range(num, 0, -1):
        f*=c
    return f
f1 = fatorial(5)
f2 = fatorial(3)
f3 = fatorial(7)
print(f'Os resultados sao {f1},{f2},{f3}')