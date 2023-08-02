#Exercício 14:Escreva um programa que leia uma lista de números e retorne uma nova lista contendo apenas os números pares da lista original.

numeros = input('Insira uma lista de números separados por espaço: ').split()

numeros = [int(numero) for numero in numeros]

pares = [num for num in numeros if num % 2 == 0]

print(f'Os números pares são {pares}')
