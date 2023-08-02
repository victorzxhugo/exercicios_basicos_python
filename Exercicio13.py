#Exercício 13:Escreva um programa que exiba os primeiros 15 números da sequência de Fibonacci.
# A sequência começa com 0 e 1, e cada número subsequente é a soma dos dois números anteriores.

a,b = 0, 1
print(f'Inicial {a}')

for _ in range(14):
    a, b = b, a + b
    print(a)
