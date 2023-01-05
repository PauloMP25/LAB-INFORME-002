import numpy as np
n = int(input("Ingrese el valor de las filas y columnas de la matriz :"))
Matriz = np.random.random_integers(1,10,size=(n,n))
print(f"La matriz es : \n {Matriz}")
transpuesta = np.transpose(Matriz)
print(transpuesta)
