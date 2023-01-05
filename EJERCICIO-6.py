import numpy as np
def crearMatriz(n,m):
    print("*Insertar los valores de la matriz por filas*")
    Matriz = []
    for nfila in range (1,n+1):
        fila = []
        print("Ingrese los valores de la fila",nfila)
        for columna in range (1,m+1):
            while True:
                try:
                    fila.append(int(input("Escriba el valor: ")))
                    break
                except ValueError:
                    print("*Ingrese un valor correcto*")
                    continue
        Matriz.append(fila)   
    return Matriz
print("** Creando Matriz A **")
n1 = int(input("Ingrese el valor de ""n"" numero de filas: "))
m1 = int(input("Ingrese el valor de ""m"" numero de columnas: "))
print("Valores de la Matriz A")
MatrizA = crearMatriz(n1,m1)
print("** Creando Matriz B **")
n2 = int(input("Ingrese el valor de ""n"" numero de filas: "))
m2 = int(input("Ingrese el valor de ""m"" numero de columnas: "))
print("Valores de la Matriz B")
MatrizB = crearMatriz(n2,m2)
matrizA = np.array(MatrizA,ndmin=n1)
matrizB = np.array(MatrizB,ndmin=n2)
producto = np.multiply(matrizA,matrizB)
print(f"Producto de matrices AB: \n{producto} ")