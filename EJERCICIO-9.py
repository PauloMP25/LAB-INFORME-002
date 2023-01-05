import numpy as np
n = int(input("Ingrese el valor de las filas y columnas de la matriz :"))
Matriz = np.random.random_integers(1,10,size=(n,n))
MatrizSimetrica = (Matriz + Matriz.T)/2
print(MatrizSimetrica)
print("Matriz Transpuesta de la matriz Simetrica")
print(MatrizSimetrica.T)
