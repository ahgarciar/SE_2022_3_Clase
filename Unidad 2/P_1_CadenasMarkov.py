import numpy as n

mTransicion = [
    [0.2,0.15,0.25,0.05,0.3,0.05],
    [0.05,0.1,0.4,0.2,0.25,0],
    [0.1,0.4,0.25,0.1,0.05,0.1],
    [0.2,0.3,0.23,0.02,0.05,0.2],
    [0.3,0.01,0.09,0.1,0.35,0.15],
    [0.5,0.3,0.02,0.1,0.07,0.01]
]

mE = [0.1,0,0.6,0.2,0.05,0.05]

matrizTransicion = n.array(mTransicion)
matrizEstadosIniciales = n.array(mE)

print("Matriz Transicion:",matrizTransicion)
print("\nMatriz E. Iniciales:",matrizEstadosIniciales)


P1 = matrizEstadosIniciales.dot(matrizTransicion)
print("P1:", P1)
P2 = P1.dot(matrizTransicion)
print("P2:", P2)
P3 = P2.dot(matrizTransicion)
print("P3:", P3)