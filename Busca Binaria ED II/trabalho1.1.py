import random

tam_lista = 100
lista = [random.randint(0, 100) for _ in range(tam_lista)]
print(lista)

x = int(input("Digite um valor a ser encontrado:"))
cont = 0

for i, valor in enumerate(lista):
    if valor == x:
        print("Valor encontrado na posição:", i)
        break
    cont+=1
print("Foram feitas ",cont,"verificações")
