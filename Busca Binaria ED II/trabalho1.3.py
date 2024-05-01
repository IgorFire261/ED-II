import random

def busca_binaria(lista, valor, contador):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            return meio, contador
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
        contador += 1

    return -1, contador


tam_lista = 100
lista = [random.randint(0, 100) for _ in range(tam_lista)]

lista.sort()
print(lista)

x = int(input("Digite um valor a ser encontrado:"))
cont = 0
resultado, cont = busca_binaria(lista, x, cont)

if resultado != -1:
    print(f'O elemento {x} está na posição {resultado} com {cont} verificações')
else:
    print(f'O elemento {x} não foi encontrado na lista')
