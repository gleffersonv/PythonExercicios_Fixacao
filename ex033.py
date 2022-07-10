'''Faça um programa que leia tres números e mostra quel é o maior e qual é o menor'''

a = input('Digite primeiro numero: ')
b = input('Digite o segundo numero: ')
c = input('Digite o terceiro numero: ')
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = c
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior numero digitado foi {}'.format(maior))
