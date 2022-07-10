''' Faça um programa que calcule a soma entre todos os números
que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''

soma = 0
vezes = 0
for contador in range(1,501, 2):
    if contador % 3 == 0:
        vezes = vezes + 1
        soma = soma + contador
print('A soma de todos {} numeros  solicitados é {}'.format(vezes, soma))
