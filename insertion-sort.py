# Insertion sort. Complejidad: O(n²)

lista = [7, 5, 3, 8, 4, 10, 1]

for indice in range(1, len(lista)):
    #Guardamos el elemento actual para que no se pierda
    actual = lista[indice]
    
    #Recorremos los elementos a la izquierda del actual con indice mayor a 0 y si el numero a la izquierda es mayor lo vamos sustituyendo
    while indice > 0 and lista[indice - 1] > actual:
        lista[indice] = lista[indice-1]
        indice -= 1
    #Guardamos el elemento actual luego de revisar que todos sus elementos a la izquierda no fueran mayores
    lista[indice] = actual
    
print(lista)