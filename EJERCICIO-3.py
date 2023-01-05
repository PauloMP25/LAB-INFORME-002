from numpy import empty
def crearListaDeTamañoEspecifico(n):
    listaNueva = []
    for i in range(0,n):
        listaNueva.append(None)
    return listaNueva

def rellenarArray(lista,numero):
    listaNueva = lista
    posicion = 0
    for contador in range(1,len(lista)+1):
        producto = numero*contador
        listaNueva[posicion] = producto
        posicion+= 1
        if posicion == len(lista):
            break
    return listaNueva

tamaño = int(input("Ingrese el tamaño del array: "))
lista1 = empty(tamaño)
numero = int(input("Ingrese el número a rellenar :"))
lista2 = crearListaDeTamañoEspecifico(tamaño)
lista1 = rellenarArray(lista1 ,numero)
lista2 = rellenarArray(lista2,numero)
print("Los múltiplos de ",numero," son:")
print(lista1)
print(lista2)
