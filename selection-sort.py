# Selection sort. Complejidad: O(n²)

lista = [5, 7, 3, 1, 4, 2, 6]

lenght = len(lista)

#Se elemento por elemento y comparamos con los siguientes, se hace hasta el lenght-1 porque cuando llega al ultimo ya no tiene con quien comparar
for indice_actual in range(lenght-1):
    #Aqui se ira guardando el indice del numero menor en sucesivas comparaciones que al principio empieza siendo el actual
    indice_numero_menor = indice_actual
    
    #Se recorre el indice mas uno para ir comparando el primer valor con los demas
    for indice_comparacion in range(indice_actual+1, lenght):
        
        #Si el numero nuevo comparado es menor al numero que tenia entonces se modifica el indice del numero menor
        if lista[indice_comparacion] < lista[indice_numero_menor]:
            indice_numero_menor = indice_comparacion

    # Se guarda el valor menor temporal de esta recorrida para luego poder hacer el intercambio
    numero_menor_temporal = lista[indice_numero_menor]
    #Se sustituye el numero que se tiene en el indice actual por donde esta el numero menor
    lista[indice_numero_menor] = lista[indice_actual]
    #El numero menor se guarda en el indice actual
    lista[indice_actual] = numero_menor_temporal
    
print(lista)