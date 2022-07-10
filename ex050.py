'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

soma = 0
cont = 0
pares = 0
for numero in range(1,7):
    n1=int(input('Digite um numero: '))
    if n1 % 2 == 0:
        soma +=  n1
        pares += 1
    cont += 1
print('Você digitou {} numeros,somente {} são PARES e a soma total deles é {}'.format(cont,pares, soma))
