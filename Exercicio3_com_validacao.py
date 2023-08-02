#Escreva um programa que solicite dois números ao usuário e exiba a soma deles.

numeros = []
numeros.append(input('Digite o primeiro numero: '))
numeros.append(input('Digite o segundo numero: '))
valida = True

def verificacao_interios(numero) -> bool:
    while True:
        try:
            int (numero)
            return True
        except ValueError as e:
            print(f'O valor "{numero}" não é numerico')
            print(f'Erro: {e}')
            return False

for n in numeros:
    if verificacao_interios(n) is False:
        valida = False

if valida:
    print(f'O valor da soma do numero {numeros[0]} e {numeros[1]} é: {int(numeros[0]) + int(numeros[1])}')
