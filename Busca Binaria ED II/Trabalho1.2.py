import random

tam_lista = 100
lista = [random.randint(0, 100) for _ in range(tam_lista)]
print(lista)

x = int(input("Digite um valor a ser encontrado:"))
flag = False  
cont = 0
vezes = 0
for i, valor in enumerate(lista):
    if valor == x:
        flag = True
        print("Valor encontrado na posição:", i)
        vezes+=1
    cont+=1
print(f'Valor encontrado {vezes} vezes')
if not flag:
    print("Valor não encontrado na lista.")
print("Foram feitas ",cont,"verificações")
