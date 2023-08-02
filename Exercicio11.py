#Exercício 11: Escreva um programa que crie uma lista de números pares de 0 a 20 (inclusive) e exiba a lista.

lista_pares = []
for num in range(0,21):
   if num % 2 == 0:
    lista_pares.append(num)

print(lista_pares)

