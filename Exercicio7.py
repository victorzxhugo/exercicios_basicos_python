# Exercício 7: Escreva um programa que peça ao usuário para digitar uma temperatura em Celsius e converta-a para Fahrenheit.
# A fórmula de conversão é: Fahrenheit = (Celsius * 9/5) + 32.

celsius = float(input('Digite uma temperatura em celsius'))
fahrenheit = (celsius * 9/5) + 32
print(f'Temperatura em fahrenheit é: {fahrenheit}')
