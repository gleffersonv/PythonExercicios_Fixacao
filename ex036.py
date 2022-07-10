'''Escreve um programa para aprovar o emprestimo bancario para a compra de uma casa.
o programa vai perguntar o:
valor da casa
o salario do comprador
e em quantas anos ele vai pagar.Calcule o valor da prestação mensal sabendo qe ela não pode exceder
30% do salário ou entao o emprestimo sera negado'''

valor_casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o salario atualizado do comprador? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
prestacao = valor_casa / (anos * 12)
maximo = (salario*30)/100
if prestacao > maximo:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação sera de R${:.2f}'.format(valor_casa, anos, prestacao))
    print('Emprestimo negado')
else:
    print('Para pagar uma casa de {:.2f} em {} anos a prestação sera de {:.2f}'.format(valor_casa, anos, prestacao))
    print('Emprestimo aprovado')