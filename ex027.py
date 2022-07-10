'''Faça um programa que leia o nome completo de uma pessoa,mostrando em seguida o primeiro e o últomo nome separadamente.
EX: Glefferson Olimpio Vicente
PRIMEIRO: GLEFFERSON
ULTIMO: VICENTE'''

nome=str(input('Digite seu nome completo: ')).strip()
fatiado= nome.split()
print('Seu primeiro nome é {}'.format(fatiado[0]))
print('Seu último nome é {}'.format(fatiado[-1]))
#ou
print('Seu último nome é {}'.format(fatiado[len(fatiado)-1]))
