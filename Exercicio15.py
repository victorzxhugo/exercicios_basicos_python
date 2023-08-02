#xercício 15:Escreva um programa que crie um dicionário com 5 pares de chave-valor, onde as chaves sejam nomes de
# frutas e os valores sejam a quantidade de cada fruta.

frutas = {
    'jabuticaba': 123123,
    'melancia': 1,
    'kiwi': 32,
    'pitaya': 10,
    'uva': 100
}
qtd = frutas.get('jabuticaba')
print(f'Existem {qtd} jabuticabas')
print(frutas)

#for f in frutas.keys():
  #  print(f)
