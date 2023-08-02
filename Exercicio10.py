#Exercício 10: Escreva um programa que peça ao usuário para digitar uma palavra e verifique se é um palíndromo
# (uma palavra que se lê da mesma forma de trás para frente).

palavra = input('Escreva uma palavra: ')

if palavra == palavra [::-1]:
    print(f'A palavra "{palavra}" é um palindromo')

else:
    print(f'A palavra "{palavra}" não é um palindromo')

