'''Desenvolva uma logica que leia o peso a altura de uma pessoa,calcule seu imc e mostre seu status
de acordo com a tabela abaixo
abaixo de 18.5: abaixo do peso
entre 18.5 e 25: peso ideal
25 ate 30: sobrepeso
30 ate 40: obesidade
acima de 40: obesidade morbida'''

peso = float(input('Digite seu PESO: (KG)'))
altura = float(input('Digite sua ALTURA: (m) '))
imc= peso/(altura**2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc == 18.5 or imc < 25:
    print('PESO IDEAL')
elif imc == 25 or imc < 30:
    print('SOBREPESO')
elif imc == 30 or imc < 40:
    print('OBESIDADE')
else:
    print('BESIDADE MORBIDA')
