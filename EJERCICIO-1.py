def almacenarNombres(tamaño):
    lista = []
    for i in range(tamaño):
        lista.append(input("Ingrese un nombre : "))
    return lista
def almacenarLongitud(tamaño,lista):
    longitudCadena =[]
    for elemento in range(len(lista)):
        longitudCadena.append(len(lista[elemento]))
    return longitudCadena

tamaño = int(input("Ingresa el tamaño del arreglo : "))
nombres = almacenarNombres(tamaño)
tamañoNombres = almacenarLongitud(tamaño,nombres)
for posicion in range(0,len(nombres)):
    print("El nombre es :",nombres[posicion]," y la longitud es :",tamañoNombres[posicion])



