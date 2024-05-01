import random

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]


tam_lista = 100
lista = [random.randint(0, 100) for _ in range(tam_lista)]
print("Lista não ordenada: \n")
print(lista)
bubblesort(lista)
print("Lista Ordenada: \n")
print(lista)


