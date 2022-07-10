''' Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''

numero=int(input('Digite um numero da tabuada? '))
for somador in range(1,11):
    print('{} X {:2} = {}'.format(numero,somador,numero*somador))
print('PRONTINHO')