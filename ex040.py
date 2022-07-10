'''Crie um programa que leia duas notas de um aluno e calcule sua media,mostrando uma mensagem no final
de acordo com a media atingida
media abaixo de 5.0: reprovado
media entre 5.0 e 6.9: recuperação
media 7.0 ou superior : aprovado'''

n1=float(input('Digite a PRIMEIRA nota: '))
n2=float(input('Digite a SEGUNDA nota: '))
media= (n1 + n2)/2
if media < 5.0:
    print('Você foi REPROVADO')
elif media == 5.0 or media < 6.9:
    print('Você esta de RECUPERAÇÃO')
elif media >= 7.0:
    print('Você foi APROVADO')
