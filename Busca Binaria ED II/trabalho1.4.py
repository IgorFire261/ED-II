import random

def busca_binaria(lista, valor,contador):
    ocorrencias = []
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        contador+=1
        if lista[meio] == valor:
            ocorrencias.append(meio)
            inicio = meio + 1
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return ocorrencias,contador


tam_lista = 100
lista = [random.randint(0, 100) for _ in range(tam_lista)]
lista.sort()
print(lista)
cont = 0
x = int(input("Digite um valor a ser encontrado:"))

ocorrencias, cont = busca_binaria(lista, x,cont)

if ocorrencias:
    print(f'O elemento {x} foi encontrado nas posições {ocorrencias} e {cont} verificações')
else:
    print(f'O elemento {x} não foi encontrado na lista')
