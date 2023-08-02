# Exercício 5: Escreva um programa que verifique se um número digitado pelo usuário é par ou ímpar.

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('Número par')
else:
    print('Numero ímpar')