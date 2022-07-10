'''Elabore um programa que calcule o valor a ser pago por um produto considerando
seu preso narmal
 e condição de pagamento
 a vista dinheiro/cheque:10% de desconto
 a vista no cartão:5% de desconto
 em ate 2xno cartão: preco normal
 3x ou mais no cartão 20% de juros'''

print('{:=^40}'.format(' LOJAS VICENTS '))
vlr= float(input('Digite o valor do produto: R$'))
print('''
[1] - Dinheiro/Cheque (A vista): 10% Desconto
[2] - Cartão (A vista) : 5% Desconto
[3] - Cartão ( max 2x) : Sem Juros
[4] - Cartão (3x ou + ) : 20% de Juros''')

opcao= int(input('Qual forma de pagamento? '))

if opcao == 1:
    total= vlr - ((vlr*10)/100)
elif opcao == 2:
    total = vlr - ((vlr*5)/100)
elif opcao == 3:
    total = vlr
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = vlr + ((vlr*20)/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = vlr
    print('Opcão invalida de pagamento. Tente novamente')
print('Sua compra é R${:.2f} , e vai custar  R${:.2f} no final'.format(vlr, total))