

def getVector(n):
    vector = []
    import random as rnd
    for i in range(n):  # del 0 al n-1
        x = rnd.randint(0, 1)
        vector.append(x)
    return vector

def getPesoVector(vector):
    peso = sum(vector)
    return peso

n = input("Ingresa el total de elementos del vector")
n = int(n)

v = getVector(n)
print(v)

p = getPesoVector(v)
print("Peso del vector:", p)