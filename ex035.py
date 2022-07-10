'''Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se ele
podem ou não formar um triangulo.'''

r1=float(input('Qual tamanho da primeira reta: '))
r2=float(input('Qual tamanho da segunda reta: '))
r3=float(input('Qual tamanho da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima podem formar um triângulo')
else:
    print('As retas acima não podem dormar triângulo')
