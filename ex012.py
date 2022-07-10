preco=float(input('Qual valor do produto? '))
desconto=preco-(preco*5/100)
print('O produto que custava R${:.2f},na promoção com 5% de desconto ele vai custar R${:.2f}'.format(preco,desconto))