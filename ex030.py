'''Crie um programa que leia um número inteiro e moestre na tela se ele é
PAR ou IMPAR'''

numero=int(input('Digite um numero inteiro: '))
resultado= numero % 2
if resultado == 0:
    print('Este numero {} é par'.format(numero))
else:
    print('Este numero {} é impar'.format(numero))
