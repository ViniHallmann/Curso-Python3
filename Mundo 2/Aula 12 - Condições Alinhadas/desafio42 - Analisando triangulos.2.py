print('Analisador de triângulo')

seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o segundo segmento: '))
seg3 = float(input('Digite o terceiro segmento: '))


if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 <seg1 + seg2:
    if seg1 == seg2 == seg3:
        print('Este triângulo é EQUILÁTERO')
        print('Os segmentos acima PODEM FORMAR um triângulo')
    elif seg1 != seg2 != seg3 != seg1:
        print('Este triângulo é ESCALENO')
        print('Os segmentos acima PODEM FORMAR um triângulo')
    else: 
        print('Este triângulo é ISÓCELES')
        print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')