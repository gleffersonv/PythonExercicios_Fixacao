'''Escreva um programa que leia dois numeros inteiros e compare-se mostrando na tela uma mensagem
o primeiro valor emaior
o segundo valor e maior
nao existe valor maios,os dois são iguais'''

n1=int(input('Digite o PRIMEIRO numero: '))
n2=int(input('Digite o SEGUNDO numero: '))
if n1 > n2:
    print('O PRIMEIRO valor é MAIOR')
elif n2 > n1:
    print('O SEGUNDO valor é MAIOR')
else:
    print('Não existe valor maior, os dois são iguais')