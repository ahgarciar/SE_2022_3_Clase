

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

def getMax(vectorPesos):
    max = -1
    for i in range(len(vectorPesos)):
        if(max < vectorPesos[i]):
            max = vectorPesos[i]
    return max

mVectores = []
mPesoVectores = []

m = 5 ##
n = 8

##Generacion de los m Vectores
for i in range(m):
    Vi = getVector(n)
    mVectores.append(Vi)

##Calculo de los m Pesos
for i in range(m):
    Peso = getPesoVector(mVectores[i])
    mPesoVectores.append(Peso)

##
##visualizacion de los vectores
for i in range(len(mVectores)):
    print(mVectores[i])

print("Peso de los Vectores: ", mPesoVectores)

maxPeso = getMax(mPesoVectores)
print("Mayor Peso: ", maxPeso)