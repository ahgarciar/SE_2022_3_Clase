def getVector(n):
    vector = []
    import random as rnd
    for i in range(n):  # del 0 al n-1
        x = rnd.randint(0, 1)
        vector.append(x)
    return vector

def getMutaVector(vector):
    import random as rnd
    vNuevo = vector[:] ##genera una copia del vector original
    for i in range(len(vector)):
        pMuta = rnd.random()
        if pMuta>= 0.5:
            pSerCeroUno = rnd.random()
            if pSerCeroUno >= 0.5:
                vNuevo[i] = 1
            else:
                vNuevo[i] = 0
    print(vNuevo)

n = 10

v = getVector(n)
print(v)


