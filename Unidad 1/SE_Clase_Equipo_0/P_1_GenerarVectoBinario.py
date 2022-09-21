
n = input("Ingresa el total de elementos del vector")
n = int(n)

vector = []

import random as rnd

for i in range(n): # del 0 al n-1
    x = rnd.randint(0,1)
    vector.append(x)

print(vector)

