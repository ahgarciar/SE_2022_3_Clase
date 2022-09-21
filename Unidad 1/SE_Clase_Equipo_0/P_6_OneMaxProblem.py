
def getVector(m):
    vector = []
    import random as rnd
    for i in range(m):  # del 0 al m-1
        x = rnd.randint(0, 1)
        vector.append(x)
    return vector

#
def getPesoVector(vector):
    peso = sum(vector)
    return peso

def getMax(vectorPesos):
    max = -1
    for i in range(len(vectorPesos)):
        if(max < vectorPesos[i]):
            max = vectorPesos[i]
    return max

#########################################################

def getPadre(mVectores, mPesoVectores):
    import random
    p1 = random.randint(0, len(mVectores)-1)
    p2 = random.randint(0, len(mVectores)-1)
    pesoP1 = mPesoVectores[p1]
    pesoP2 = mPesoVectores[p2]
    print("Padres seleccionados: ", p1,"(Peso:",pesoP1,")", " y ", p2,"(Peso:",pesoP2,")")
    if pesoP1> pesoP2:
        pSel = p1
    else:
        pSel = p2
    print("Padre ganador: ", pSel)
    return pSel
##############################################################

mVectores = []
mPesoVectores = []

n = 10 #total Vectores
m = 7 #total de elementos de los vectores

it = 1 #iteraciones

#Generar vectores iniciales
#mVectores = []

for i in range(10):
    v = getVector(m) #generar vector aleatorio
    mVectores.append(v) #añadirlo a la lista de vectores
    mPesoVectores.append(getPesoVector(v)) #añadir el peso del vector

mVectoresTemporales = []
import random
for i in range(it):
    print(i + 1)
    #seleccion
    #Para pSel1
    indexPadre1 = getPadre(mVectores,mPesoVectores)
    indexPadre2 = getPadre(mVectores, mPesoVectores)
    print()
    #####################################
    #cruza
    hijo1, hijo2 = cruza(mVectores[indexPadre1], mVectores[indexPadre2])
    #muta
    hijo1 = muta(hijo1)
    hijo2 = muta(hijo2)
    #
    #add new vectors
    mVectores.append(hijo1)
    mVectores.append(hijo2)
    ##
    #ordenar mVectores por peso, de mayor a menor

    #mVectores debe deshacerse de los vectores con menos peso
    #que se encuetren de sobra
