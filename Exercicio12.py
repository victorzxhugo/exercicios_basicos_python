#Exercício 12: Escreva um programa que solicite um número ao usuário e verifique se ele é positivo, negativo ou zero.

numero = float(input('Digite um número: '))

if numero > 0:
    print('Número positivo')
elif numero < 0:
    print('Número negativo')
else:
    print('Número zero')
